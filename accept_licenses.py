#!/usr/bin/env python3
"""
Android SDK License Acceptance Script
This script automatically accepts all Android SDK licenses.
"""

import os
import subprocess
import tempfile

def accept_android_licenses():
    """Accept all Android SDK licenses by creating a temporary license acceptance input file."""
    print("Accepting Android SDK licenses...")
    
    # Create a temporary file with "y" answers
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        for _ in range(100):  # More than enough "y" responses
            tmp.write("y\n")
        tmp_path = tmp.name
    
    try:
        # Set up environment variables
        env = os.environ.copy()
        android_sdk_root = os.path.expanduser("~/.briefcase/tools/android_sdk")
        
        # Run briefcase to create android project - this will trigger license acceptance
        command = ["python", "-m", "briefcase", "create", "android"]
        
        print(f"Running command: {' '.join(command)}")
        print(f"Using input file with 'y' responses: {tmp_path}")
        
        with open(tmp_path, 'r') as input_file:
            result = subprocess.run(
                command,
                stdin=input_file,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                env=env
            )
        
        print("Command output:")
        print(result.stdout)
        
        if result.returncode == 0:
            print("Licenses accepted successfully.")
            return True
        else:
            print(f"License acceptance failed with exit code: {result.returncode}")
            return False
            
    except Exception as e:
        print(f"Error during license acceptance: {e}")
        return False
    finally:
        # Clean up temporary file
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

if __name__ == "__main__":
    accept_android_licenses()