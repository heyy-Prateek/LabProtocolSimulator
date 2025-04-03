"""
Android Application Bridge for Chemical Engineering Lab Simulator

This is the main entry point for the Android app. The actual logic is in the
chemengsim package.
"""

from chemengsim.android_app import main

if __name__ == '__main__':
    app = main()
    app.main_loop()