#!/bin/bash

echo "==================================================="
echo "Chemical Engineering Lab Simulator - Android Builder"
echo "==================================================="
echo ""
echo "This script will build an Android APK for the Chemical Engineering Lab Simulator."
echo ""
echo "Checking for required tools..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed or not in PATH."
    echo "Please install Python 3.8 or newer and try again."
    exit 1
fi

echo "Python found!"
echo ""
echo "Setting up build environment..."

# Check if virtual environment exists, if not create one
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install required packages
echo "Installing required packages..."
pip install setuptools wheel pip --upgrade
pip install briefcase toga toga-android matplotlib numpy pandas scipy streamlit kivy kivymd

echo "Environment setup complete!"
echo ""
echo "Building Android APK..."

# Run build script
python3 build_android.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Error: Build failed. Please check the logs above for details."
    exit 1
fi

echo ""
echo "==================================================="
echo "Build completed successfully!"
echo ""
echo "Your APK file should be available in the dist directory."
echo ""
echo "To install on an Android device:"
echo "1. Connect your device via USB"
echo "2. Enable Developer Options and USB Debugging"
echo "3. Copy the APK file to your device and install it"
echo "==================================================="

# Make the script executable
chmod +x build_android.py