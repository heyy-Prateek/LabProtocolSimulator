# Android Build Guide for Chemical Engineering Lab Simulator

This guide provides detailed instructions on how to build the Android APK for the Chemical Engineering Lab Simulator application on your own system.

## Prerequisites

Before starting, ensure you have the following installed:
- Python 3.8 or later
- JDK 11 or later
- Android SDK (can be installed via Android Studio)
- Android NDK
- Briefcase (`pip install briefcase`)
- Git (for cloning the repository)

## Setting Up Your Environment

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chemical-engineering-lab-simulator
   ```

2. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Set environment variables:
   - `ANDROID_SDK_ROOT` pointing to your Android SDK directory
   - `JAVA_HOME` pointing to your JDK installation

## Building the APK

### Option 1: Using the Build Script

1. Run the build script:
   ```
   python build_android.py
   ```
   or on Windows:
   ```
   build_android.bat
   ```

2. When prompted, accept all Android SDK licenses.

3. Wait for the build process to complete. This may take several minutes depending on your system's performance.

4. The final APK will be located in one of the following directories:
   - `build/chemengsim/android/app/build/outputs/apk/debug/app-debug.apk`
   - `build/ChemicalEngineeringLabSimulator/android/app/build/outputs/apk/debug/app-debug.apk`

### Option 2: Manual Build Process

1. Create the Android project structure:
   ```
   python -m briefcase create android
   ```

2. Build the Android APK:
   ```
   python -m briefcase build android
   ```

3. The APK will be located in the same directories as mentioned in Option 1.

## Troubleshooting

### License Issues

If you encounter license acceptance issues:
1. Run `sdkmanager --licenses` from your Android SDK's tools/bin directory
2. Accept all licenses by typing 'y' when prompted

### Build Failures

1. Check that all required environment variables are set correctly
2. Ensure your Android SDK has all required components:
   - Android SDK Build-Tools
   - Android SDK Command-line Tools
   - NDK
   - Android SDK Platform for the target API level (26+)

3. If the build fails with Java-related errors, ensure you're using JDK 11
   ```
   java -version
   ```

4. Clean the project and try again:
   ```
   python -m briefcase clean android
   python -m briefcase create android
   python -m briefcase build android
   ```

## Installing the APK

After building:

1. Transfer the APK to your Android device
2. Enable "Install from Unknown Sources" in your device settings
3. Use a file manager to locate and install the APK

## Features of the Android Application

The Android version of Chemical Engineering Lab Simulator includes:

- Interactive simulations for all 10 chemical engineering experiments
- Quiz mode for testing your knowledge
- Video demonstrations of experiments
- Complete offline functionality
- Touch-optimized interface

## Minimum Requirements

- Android 8.0 or higher
- 2GB of RAM
- 100MB of free storage space

## Support

For any issues or questions about the Android build process, please open an issue in the repository or contact the development team.

----

© 2025 Chemical Engineering Lab Simulator