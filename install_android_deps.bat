@echo off
echo ===================================================
echo Android Dependencies Installer for CE Lab Simulator
echo ===================================================
echo.
echo This script will help install the necessary Android SDK and NDK components
echo required to build the Chemical Engineering Lab Simulator as an Android app.
echo.

REM Set the current directory as the working directory
cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3.8 or newer and try again.
    goto :error
)

REM Activate virtual environment if it exists or create it
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    if %ERRORLEVEL% NEQ 0 goto :error
)

call venv\Scripts\activate.bat
if %ERRORLEVEL% NEQ 0 goto :error

REM Install Briefcase which will download Android SDK/NDK
echo Installing Briefcase...
python -m pip install --upgrade pip
python -m pip install briefcase==0.3.14

REM Check for Java JDK
echo Checking for Java JDK...
java -version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Java JDK not found. 
    echo Please install JDK 11 or newer from: https://adoptium.net/
    echo After installing Java, restart this script.
    goto :error
)

REM Run briefcase to download Android SDK automatically
echo.
echo Downloading Android SDK and NDK (this may take a while)...
echo.

REM Create a temporary Python script to download SDK
echo import sys > download_sdk.py
echo import os >> download_sdk.py
echo import subprocess >> download_sdk.py
echo from pathlib import Path >> download_sdk.py
echo print("Setting up Android SDK and NDK...") >> download_sdk.py
echo try: >> download_sdk.py
echo     import briefcase >> download_sdk.py
echo     from briefcase.platforms.android.gradle import GradleAndroidBuildCommand >> download_sdk.py
echo     cmd = GradleAndroidBuildCommand(sys.argv[1:]) >> download_sdk.py
echo     cmd.bundle_path("dummy") >> download_sdk.py
echo     print("Android SDK and NDK downloaded successfully") >> download_sdk.py
echo except Exception as e: >> download_sdk.py
echo     print(f"Error: {e}") >> download_sdk.py
echo     sys.exit(1) >> download_sdk.py

python download_sdk.py verify-app

if %ERRORLEVEL% NEQ 0 (
    echo Failed to download Android SDK.
    goto :error
)

REM Clean up
del download_sdk.py

REM Accept all licenses
echo.
echo Accepting Android SDK licenses...
python accept_licenses.py

if %ERRORLEVEL% NEQ 0 (
    echo Failed to accept licenses. You may need to accept them manually.
)

echo.
echo ===================================================
echo Android dependencies installed successfully!
echo.
echo You can now run build_android.bat to build the APK.
echo ===================================================
goto :end

:error
echo.
echo Error: Installation failed. Please check the logs above for details.

:end
pause 