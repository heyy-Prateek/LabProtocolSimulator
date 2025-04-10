"""
Build script for the React frontend.

This script builds the React frontend and copies the output to the correct location.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def build_react_app():
    """Build the React frontend and copy to the static folder"""
    # Get the directory of this script
    script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    
    # Set paths
    react_src_dir = script_dir / "react_src"
    react_build_dir = script_dir / "react_build"
    
    # Create node_modules and package.json if not exists
    if not os.path.exists(react_src_dir / "package.json"):
        print("Creating package.json...")
        package_json = {
            "name": "chemengsim-ui",
            "version": "0.1.0",
            "private": True,
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "react-router-dom": "^6.8.1",
                "styled-components": "^5.3.6"
            },
            "scripts": {
                "start": "react-scripts start",
                "build": "react-scripts build",
                "test": "react-scripts test",
                "eject": "react-scripts eject"
            },
            "eslintConfig": {
                "extends": [
                    "react-app"
                ]
            },
            "browserslist": {
                "production": [
                    ">0.2%",
                    "not dead",
                    "not op_mini all"
                ],
                "development": [
                    "last 1 chrome version",
                    "last 1 firefox version",
                    "last 1 safari version"
                ]
            }
        }
        
        with open(react_src_dir / "package.json", "w") as f:
            import json
            json.dump(package_json, f, indent=2)
    
    # Install dependencies if node_modules doesn't exist
    if not os.path.exists(react_src_dir / "node_modules"):
        print("Installing dependencies...")
        subprocess.run(["npm", "install"], cwd=react_src_dir, shell=True, check=True)
    
    # Build the React app
    print("Building React app...")
    subprocess.run(["npm", "run", "build"], cwd=react_src_dir, shell=True, check=True)
    
    # Create the build directory if it doesn't exist
    os.makedirs(react_build_dir, exist_ok=True)
    
    # Copy the build output to the static folder
    print("Copying build output to static folder...")
    build_output_dir = react_src_dir / "build"
    if os.path.exists(build_output_dir):
        # Remove previous build files
        if os.path.exists(react_build_dir):
            shutil.rmtree(react_build_dir)
        
        # Copy new build files
        shutil.copytree(build_output_dir, react_build_dir)
        print(f"React build completed successfully. Output copied to {react_build_dir}")
    else:
        print(f"Error: Build output directory not found at {build_output_dir}")
        return False
    
    return True

def main():
    """Main function"""
    try:
        success = build_react_app()
        if success:
            print("React frontend build completed successfully!")
        else:
            print("Failed to build React frontend.")
            sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 