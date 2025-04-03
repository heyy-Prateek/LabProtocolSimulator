#!/usr/bin/env python3
"""
Check Package Structure for Chemical Engineering Lab Simulator
This script verifies that the package structure is correct and all imports work properly.
"""

import sys
import importlib
import pkgutil

def check_imports(package_name):
    """Check that all modules in the package can be imported."""
    try:
        package = importlib.import_module(package_name)
        print(f"✓ Successfully imported {package_name}")
        
        # Check all subpackages and modules
        for _, name, is_pkg in pkgutil.iter_modules(package.__path__, package.__name__ + '.'):
            try:
                importlib.import_module(name)
                print(f"  ✓ Successfully imported {name}")
                
                # If it's a subpackage, we need to check its modules too
                if is_pkg:
                    subpkg = importlib.import_module(name)
                    for _, subname, _ in pkgutil.iter_modules(subpkg.__path__, subpkg.__name__ + '.'):
                        try:
                            importlib.import_module(subname)
                            print(f"    ✓ Successfully imported {subname}")
                        except ImportError as e:
                            print(f"    ✗ Failed to import {subname}: {e}")
            except ImportError as e:
                print(f"  ✗ Failed to import {name}: {e}")
    except ImportError as e:
        print(f"✗ Failed to import {package_name}: {e}")

def main():
    """Main function to check package structure."""
    print("=== Chemical Engineering Lab Simulator - Package Check ===")
    
    print("\nChecking main package:")
    check_imports('chemengsim')
    
    print("\nChecking experiments subpackage:")
    check_imports('chemengsim.experiments')
    
    print("\nChecking quizzes subpackage:")
    check_imports('chemengsim.quizzes')
    
    print("\nChecking videos subpackage:")
    check_imports('chemengsim.videos')
    
    print("\nPackage check completed.")

if __name__ == "__main__":
    main()