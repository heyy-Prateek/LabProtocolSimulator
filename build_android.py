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
from pathlib import Path

def setup_environment():
    """Set up the build environment and check for required dependencies."""
    print("Setting up build environment...")
    
    # Check if required packages are installed
    try:
        import briefcase
        print(f"Using Briefcase version {briefcase.__version__}")
    except ImportError:
        print("Briefcase not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "briefcase"])
    
    # Check if streamlit is installed
    try:
        import streamlit
        print(f"Using Streamlit version {streamlit.__version__}")
    except ImportError:
        print("Streamlit not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "streamlit"])
        
    # Check if toga is installed
    try:
        import toga
        print(f"Using Toga version {toga.__version__}")
    except ImportError:
        print("Toga not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "toga"])
    
    # Create virtual environment for the build
    print("Creating virtual environment...")
    venv_dir = Path("venv")
    if not venv_dir.exists():
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        
        # Activate virtual environment
        if sys.platform == "win32":
            pip_path = venv_dir / "Scripts" / "pip"
        else:
            pip_path = venv_dir / "bin" / "pip"
            
        # Install required packages
        subprocess.run([str(pip_path), "install", "-U", "pip", "setuptools", "wheel"], check=True)
        subprocess.run([str(pip_path), "install", "briefcase", "streamlit", "toga"], check=True)
    
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
        shutil.copy("generated-icon.png", "app_icon.png")
    
    # Copy any necessary resources
    resources_dir = Path("android_resources")
    if not resources_dir.exists():
        os.makedirs(resources_dir)
    
    print("Application files prepared.")

def build_android_app(debug=True):
    """Build the Android APK."""
    print("Building Android APK...")
    
    # Mode flag for debug or release build
    mode_flag = "--debug" if debug else "--release"
    
    try:
        # Initialize the android project if it doesn't exist
        subprocess.run([
            sys.executable, "-m", "briefcase", "create", "android",
        ], check=True)
        
        # Update the project with any changes
        subprocess.run([
            sys.executable, "-m", "briefcase", "update", "android",
        ], check=True)
        
        # Build the APK
        subprocess.run([
            sys.executable, "-m", "briefcase", "build", "android", mode_flag,
        ], check=True)
        
        # Run the app on connected device for testing (if in debug mode)
        if debug:
            print("Running app on connected Android device...")
            subprocess.run([
                sys.executable, "-m", "briefcase", "run", "android",
            ])
        
        # Package the app for distribution
        print("Packaging app for distribution...")
        subprocess.run([
            sys.executable, "-m", "briefcase", "package", "android", mode_flag,
        ], check=True)
        
        # Copy the APK to the dist directory
        for apk_file in Path("android/build/outputs/apk").glob("**/*.apk"):
            target_path = Path("dist") / apk_file.name
            shutil.copy(str(apk_file), str(target_path))
            print(f"APK generated: {target_path}")
        
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