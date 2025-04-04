@echo off
echo ===================================================
echo Chemical Engineering Lab Simulator - Android Builder
echo ===================================================
echo.
echo This script will build an Android APK for the Chemical Engineering Lab Simulator.
echo.

REM Set the current directory as the working directory
cd /d "%~dp0"

REM Check for Android SDK environment variable
if not defined ANDROID_SDK_ROOT (
    echo Checking for Android SDK...
    if exist "%LOCALAPPDATA%\Android\Sdk" (
        echo Found Android SDK at %LOCALAPPDATA%\Android\Sdk
        set ANDROID_SDK_ROOT=%LOCALAPPDATA%\Android\Sdk
    ) else (
        echo Android SDK not found. The build script will attempt to download it.
        echo If you already have Android SDK installed, set ANDROID_SDK_ROOT environment variable.
    )
) else (
    echo Using Android SDK at %ANDROID_SDK_ROOT%
)

REM Check for Android NDK environment variable
if not defined ANDROID_NDK_HOME (
    if defined ANDROID_SDK_ROOT (
        echo Checking for Android NDK...
        if exist "%ANDROID_SDK_ROOT%\ndk" (
            echo Found NDK directory. The build script will select an appropriate version.
        ) else (
            echo Android NDK not found. The build script will attempt to download it.
        )
    )
) else (
    echo Using Android NDK at %ANDROID_NDK_HOME%
)

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
python -m pip install --upgrade pip setuptools wheel
python -m pip install briefcase==0.3.14 toga==0.3.1 toga-android matplotlib numpy pandas scipy streamlit==1.27.0 kivy kivymd

echo Environment setup complete!
echo.
echo Building Android APK...

REM Accept SDK licenses automatically
echo Setting environment variable to accept licenses automatically...
set ACCEPT_ANDROID_SDK_LICENSES=yes

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
echo.
echo Common issues:
echo 1. Android SDK or NDK not properly installed
echo 2. Java JDK not installed or wrong version (JDK 11 is recommended)
echo 3. Missing Python dependencies
echo.
echo For more help, see README_ANDROID.md

:end
pause