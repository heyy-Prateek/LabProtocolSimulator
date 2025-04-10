#!/usr/bin/env python3
"""
Build Script for Android APK Generation with Auto-License Acceptance
This script automates the process of building an Android APK from the Chemical Engineering Lab Simulator.
It automatically accepts all Android SDK licenses during the build process.
"""

import os
import sys
import subprocess
import platform
import time
import shutil

def setup_environment():
    """Set up the build environment and check for required dependencies."""
    print("Setting up build environment...")
    try:
        import briefcase
        print(f"Using Briefcase version {briefcase.__version__}")
    except ImportError:
        print("Error: Briefcase not installed. Please install it with 'pip install briefcase'.")
        sys.exit(1)
    
    try:
        import streamlit
        print(f"Using Streamlit version {streamlit.__version__}")
    except ImportError:
        print("Error: Streamlit not installed. Please install it with 'pip install streamlit'.")
        sys.exit(1)
    
    try:
        import toga
        print(f"Using Toga version {toga.__version__}")
    except ImportError:
        print("Error: Toga not installed. Please install it with 'pip install toga'.")
        sys.exit(1)
    
    # Create a virtual environment for the build process
    print("Creating virtual environment...")
    # This is now handled by Briefcase
    
    print("Environment setup complete.")

def prepare_app_files():
    """Prepare application files for packaging."""
    print("Preparing application files...")
    
    # Create necessary directories if they don't exist
    os.makedirs(".streamlit", exist_ok=True)
    
    # Create Streamlit config file for Android
    with open(".streamlit/config.toml", "w") as f:
        f.write("""
[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false

[browser]
serverPort = 8501
""")
    
    # Create mobile.yaml for Streamlit
    with open(".streamlit/mobile.yaml", "w") as f:
        f.write("""
layout: one-column
""")
    
    print("Application files prepared.")

def accept_all_licenses():
    """Automatically accept all Android SDK licenses."""
    print("Accepting Android SDK licenses...")
    
    # Create a license acceptance script
    with open("accept_licenses.sh", "w") as f:
        f.write("""#!/bin/sh
yes | sdkmanager --licenses
""")
    
    # Make it executable
    os.chmod("accept_licenses.sh", 0o755)
    
    # Run the script
    try:
        subprocess.run(["./accept_licenses.sh"], check=True)
        print("Android SDK licenses accepted.")
    except subprocess.CalledProcessError:
        print("Warning: Could not automatically accept licenses. You may need to accept them manually.")
    except FileNotFoundError:
        print("Warning: Could not find sdkmanager. Continuing with build process.")
    
    # Clean up
    if os.path.exists("accept_licenses.sh"):
        os.remove("accept_licenses.sh")

def build_android_app(debug=True):
    """Build the Android APK with auto-license acceptance."""
    print("Building Android APK...")
    
    # Accept all licenses before building
    accept_all_licenses()
    
    # Set environment variable to automatically accept licenses
    os.environ['ANDROID_SDK_ROOT'] = os.path.expanduser('~/.briefcase/tools/android_sdk')
    os.environ['ACCEPT_ANDROID_SDK_LICENSES'] = 'yes'
    
    # Run the Briefcase command to create the Android app
    try:
        # Use subprocess.run to capture output
        result = subprocess.run(
            [sys.executable, "-m", "briefcase", "create", "android"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            env=os.environ
        )
        print(result.stdout)
        
        # Now build the app
        build_type = "--debug" if debug else ""
        result = subprocess.run(
            [sys.executable, "-m", "briefcase", "build", "android", build_type],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            env=os.environ
        )
        print(result.stdout)
        
        # Try to find the APK file
        apk_dir = "build/ChemicalEngineeringLabSimulator/android/app/build/outputs/apk"
        if os.path.exists(apk_dir):
            for root, dirs, files in os.walk(apk_dir):
                for file in files:
                    if file.endswith(".apk"):
                        apk_path = os.path.join(root, file)
                        print(f"APK built successfully: {apk_path}")
                        
                        # Copy the APK to the project root for easy access
                        dest_path = os.path.join(os.getcwd(), "ChemicalEngineeringLabSimulator.apk")
                        shutil.copy2(apk_path, dest_path)
                        print(f"APK copied to: {dest_path}")
                        
                        return True
        
        print("APK built, but could not locate the file.")
        return True
    
    except subprocess.CalledProcessError as e:
        print(f"Error building Android APK: {e}")
        print(e.output)
        return False

def main():
    """Main function to build the Android app with auto-license acceptance."""
    print("=== Chemical Engineering Lab Simulator - Android Build Script ===")
    
    setup_environment()
    prepare_app_files()
    
    success = build_android_app(debug=True)
    
    if success:
        print("Build process completed successfully.")
    else:
        print("Build process failed. Check the logs for details.")

if __name__ == "__main__":
    main()