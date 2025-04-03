@echo off
echo ===================================================
echo Chemical Engineering Lab Simulator - Android Builder
echo ===================================================
echo.
echo This script will build an Android APK for the Chemical Engineering Lab Simulator.
echo.
echo Checking for required tools...

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3.8 or newer and try again.
    goto :error
)

echo Python found!
echo.
echo Setting up build environment...

REM Check if virtual environment exists, if not create one
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install required packages
echo Installing required packages...
pip install setuptools wheel pip --upgrade
pip install briefcase toga toga-android matplotlib numpy pandas scipy streamlit kivy kivymd

echo Environment setup complete!
echo.
echo Building Android APK...

REM Run build script
python build_android.py

if %ERRORLEVEL% NEQ 0 goto :error

echo.
echo ===================================================
echo Build completed successfully!
echo.
echo Your APK file should be available in the dist directory.
echo.
echo To install on an Android device:
echo 1. Connect your device via USB
echo 2. Enable Developer Options and USB Debugging
echo 3. Copy the APK file to your device and install it
echo ===================================================
goto :end

:error
echo.
echo Error: Build failed. Please check the logs above for details.

:end
pause