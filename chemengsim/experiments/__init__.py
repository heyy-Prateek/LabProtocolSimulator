"""
Experiments module for Chemical Engineering Simulator.
This module provides a registry of available experiments and utilities for working with them.
"""

import os
import importlib
from typing import Dict, Any, Optional

# Dictionary to store registered experiments
_experiments = {}

def register_experiment(experiment_id: str, module: Any) -> None:
    """
    Register an experiment module with the simulator.
    
    Args:
        experiment_id: Unique identifier for the experiment
        module: Python module containing the experiment implementation
    """
    _experiments[experiment_id] = module

def get_experiments() -> Dict[str, Any]:
    """
    Get all registered experiments.
    
    Returns:
        Dictionary mapping experiment IDs to their corresponding modules
    """
    # If no experiments have been registered yet, auto-discover them
    if not _experiments:
        discover_experiments()
        
    return _experiments

def get_experiment(experiment_id: str) -> Optional[Any]:
    """
    Get a specific experiment by ID.
    
    Args:
        experiment_id: ID of the experiment to retrieve
        
    Returns:
        Experiment module if found, None otherwise
    """
    experiments = get_experiments()
    return experiments.get(experiment_id)

def discover_experiments() -> None:
    """
    Automatically discover and register experiment modules.
    
    This function searches for experiment modules in this package
    and registers them using their filename as the ID.
    """
    # List of all experiment modules to try loading
    experiment_modules = [
        "batch_reactor",
        "semi_batch_reactor",
        "cstr",
        "pfr",
        "crushers",
        "filter_press",
        "rotary_vacuum_filter",
        "centrifuge_flotation",
        "classifiers",
        "trommel"
    ]
    
    # Default attribute values
    default_attributes = {
        "name": "Unknown Experiment",
        "description": "No description provided",
        "default_parameters": {},
        "equations": [],
        "variables": {}
    }
    
    for module_name in experiment_modules:
        try:
            # Import the experiment module using absolute import
            full_module_name = f"chemengsim.experiments.{module_name}"
            module = importlib.import_module(full_module_name)
            
            # Check for required attributes and add them if missing
            for attr_name, default_value in default_attributes.items():
                if not hasattr(module, attr_name):
                    setattr(module, attr_name, default_value)
                    print(f"Added missing attribute '{attr_name}' to module '{module_name}'")
            
            # Set name based on module_name if it's the default
            if module.name == default_attributes["name"]:
                # Convert snake_case to Title Case
                module.name = " ".join(word.capitalize() for word in module_name.split("_"))
            
            # Register the experiment
            register_experiment(module_name, module)
            print(f"Registered experiment: {module_name} - {module.name}")
        except ImportError as e:
            print(f"Warning: Could not import experiment module '{module_name}': {str(e)}")
        except Exception as e:
            print(f"Error loading experiment '{module_name}': {str(e)}")

# Automatically discover experiments when the module is imported
discover_experiments()