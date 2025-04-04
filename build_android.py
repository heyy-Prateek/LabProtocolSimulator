#!/usr/bin/env python3
"""
Build Script for Android APK Generation
This script automates the process of building an Android APK from the Chemical Engineering Lab Simulator.
It uses the Briefcase tool from the BeeWare project.
"""

import os
import sys
import subprocess
import shutil
import argparse
import platform
from pathlib import Path
import tempfile

def set_android_env_vars():
    """Set Android SDK and NDK environment variables."""
    # Default paths for Android SDK based on OS
    home_dir = os.path.expanduser("~")
    
    if platform.system() == "Windows":
        android_sdk_default = os.path.join(home_dir, "AppData", "Local", "Android", "Sdk")
        if not os.environ.get("ANDROID_SDK_ROOT") and os.path.exists(android_sdk_default):
            os.environ["ANDROID_SDK_ROOT"] = android_sdk_default
            print(f"Set ANDROID_SDK_ROOT to {android_sdk_default}")
            
        # Look for NDK in the SDK directory
        if os.environ.get("ANDROID_SDK_ROOT"):
            ndk_path = os.path.join(os.environ["ANDROID_SDK_ROOT"], "ndk")
            if os.path.exists(ndk_path):
                # Find the highest version
                ndk_versions = [d for d in os.listdir(ndk_path) if os.path.isdir(os.path.join(ndk_path, d))]
                if ndk_versions:
                    latest_ndk = sorted(ndk_versions)[-1]
                    ndk_full_path = os.path.join(ndk_path, latest_ndk)
                    os.environ["ANDROID_NDK_HOME"] = ndk_full_path
                    print(f"Set ANDROID_NDK_HOME to {ndk_full_path}")
    
    # Check if the environment variables are set
    if not os.environ.get("ANDROID_SDK_ROOT"):
        print("Warning: ANDROID_SDK_ROOT is not set. Briefcase will attempt to download the Android SDK.")
    
    if not os.environ.get("ANDROID_NDK_HOME"):
        print("Warning: ANDROID_NDK_HOME is not set. Briefcase will attempt to download the Android NDK.")

def accept_android_licenses():
    """Accept all Android SDK licenses automatically."""
    print("Accepting Android SDK licenses...")
    
    # Create a temporary file with "y" answers
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        for _ in range(100):  # More than enough "y" responses
            tmp.write("y\n")
        tmp_path = tmp.name
    
    try:
        # First check if the SDK is available
        sdk_manager = None
        
        if os.environ.get("ANDROID_SDK_ROOT"):
            # Try to find sdkmanager
            if platform.system() == "Windows":
                sdk_manager = os.path.join(os.environ["ANDROID_SDK_ROOT"], "tools", "bin", "sdkmanager.bat")
                if not os.path.exists(sdk_manager):
                    sdk_manager = os.path.join(os.environ["ANDROID_SDK_ROOT"], "cmdline-tools", "latest", "bin", "sdkmanager.bat")
            else:
                sdk_manager = os.path.join(os.environ["ANDROID_SDK_ROOT"], "tools", "bin", "sdkmanager")
                if not os.path.exists(sdk_manager):
                    sdk_manager = os.path.join(os.environ["ANDROID_SDK_ROOT"], "cmdline-tools", "latest", "bin", "sdkmanager")
        
        if sdk_manager and os.path.exists(sdk_manager):
            print(f"Using sdkmanager at: {sdk_manager}")
            with open(tmp_path, 'r') as input_file:
                subprocess.run(
                    [sdk_manager, "--licenses"],
                    stdin=input_file,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )
            print("Licenses accepted successfully.")
        else:
            print("Could not find sdkmanager. Licenses will need to be accepted during the build process.")
            
    except Exception as e:
        print(f"Error during license acceptance: {e}")
    finally:
        # Clean up temporary file
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

def setup_environment():
    """Set up the build environment and check for required dependencies."""
    print("Setting up build environment...")
    
    # Set environment variables for Android SDK and NDK
    set_android_env_vars()
    
    # Accept Android licenses
    accept_android_licenses()
    
    # Check if required packages are installed
    try:
        import briefcase
        print(f"Using Briefcase version {briefcase.__version__}")
    except ImportError:
        print("Briefcase not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "briefcase==0.3.14"], check=True)
    
    # Check if streamlit is installed
    try:
        import streamlit
        print(f"Using Streamlit version {streamlit.__version__}")
    except ImportError:
        print("Streamlit not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "streamlit==1.27.0"], check=True)
        
    # Check if toga is installed
    try:
        import toga
        print(f"Using Toga version {toga.__version__}")
    except ImportError:
        print("Toga not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "toga==0.3.1"], check=True)
    
    # Create directories if they don't exist
    os.makedirs("build", exist_ok=True)
    os.makedirs("dist", exist_ok=True)
    
    print("Environment setup complete.")

def prepare_app_files():
    """Prepare application files for packaging."""
    print("Preparing application files...")
    
    # Ensure the app icon exists or create a default one
    icon_path = Path("app_icon.png")
    if not icon_path.exists():
        print("App icon not found, using default icon...")
        icon_dir = Path("android_resources")
        os.makedirs(icon_dir, exist_ok=True)
        
        if os.path.exists("generated-icon.png"):
            shutil.copy("generated-icon.png", "app_icon.png")
        else:
            print("Warning: No default icon found. Briefcase will use a placeholder icon.")
    
    # Create necessary configuration files for Streamlit
    streamlit_config_dir = Path(".streamlit")
    os.makedirs(streamlit_config_dir, exist_ok=True)
    
    # Create Streamlit config file if it doesn't exist
    config_file = streamlit_config_dir / "config.toml"
    if not config_file.exists():
        with open(config_file, "w") as f:
            f.write("""[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false
address = "127.0.0.1"

[browser]
serverPort = 8501
""")
    
    # Create mobile configuration
    mobile_config = streamlit_config_dir / "mobile.yaml"
    if not mobile_config.exists():
        with open(mobile_config, "w") as f:
            f.write("layout: one-column\n")
    
    print("Application files prepared.")

def build_android_app(debug=True):
    """Build the Android APK."""
    print("Building Android APK...")
    
    # Mode flag for debug or release build
    mode_flag = "--debug" if debug else "--release"
    
    try:
        # Set environment variable to automatically accept licenses
        os.environ['ACCEPT_ANDROID_SDK_LICENSES'] = 'yes'
        
        # Initialize the android project if it doesn't exist
        print("Creating Android project...")
        subprocess.run([
            sys.executable, "-m", "briefcase", "create", "android",
        ], check=True)
        
        # Update the project with any changes
        print("Updating Android project...")
        subprocess.run([
            sys.executable, "-m", "briefcase", "update", "android",
        ], check=True)
        
        # Build the APK
        print("Building Android APK...")
        subprocess.run([
            sys.executable, "-m", "briefcase", "build", "android", mode_flag,
        ], check=True)
        
        # Package the app for distribution
        print("Packaging app for distribution...")
        subprocess.run([
            sys.executable, "-m", "briefcase", "package", "android", mode_flag,
        ], check=True)
        
        # Copy the APK to the dist directory
        apk_found = False
        possible_apk_dirs = [
            # Check both possible output directories
            Path("android/app/build/outputs/apk"),
            Path("android/build/outputs/apk"),
            Path("build/ChemicalEngineeringLabSimulator/android/app/build/outputs/apk"),
            Path("build/chemengsim/android/app/build/outputs/apk")
        ]
        
        for apk_dir in possible_apk_dirs:
            if apk_dir.exists():
                # Try to find APK files recursively
                for root, _, files in os.walk(apk_dir):
                    for file in files:
                        if file.endswith(".apk"):
                            apk_file = Path(root) / file
                            target_path = Path("dist") / file
                            shutil.copy(str(apk_file), str(target_path))
                            print(f"APK generated: {target_path}")
                            apk_found = True
        
        if not apk_found:
            print("Warning: No APK files found in expected output directories.")
            
        print("Android APK build completed successfully.")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error building Android APK: {e}")
        return False

def main():
    """Main function to build the Android app."""
    parser = argparse.ArgumentParser(description="Build Android APK for Chemical Engineering Lab Simulator")
    parser.add_argument("--release", action="store_true", help="Build a release version instead of debug")
    args = parser.parse_args()
    
    print("=== Chemical Engineering Lab Simulator - Android Build Script ===")
    
    setup_environment()
    prepare_app_files()
    
    success = build_android_app(debug=not args.release)
    
    if success:
        print("Build process completed successfully.")
        print("APK file(s) available in the 'dist' directory.")
    else:
        print("Build process failed. Check the logs for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()