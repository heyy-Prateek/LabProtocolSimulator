"""
Main Report Generation Interface
==============================

This module provides the main interface for the report generation functionality.
"""

import streamlit as st
from .report_generator import display_report_generation_ui
from . import basket_centrifuge, froth_flotation, rotary_vacuum_filter, classifiers

def main():
    """Main function for report generation interface"""
    # Get the current experiment selection from the sidebar
    selected_experiment = st.session_state.get('selected_experiment', 'Home')
    
    if selected_experiment == "Home":
        display_report_generation_ui()
    elif selected_experiment == "8. Centrifuge and Flotation":
        # Create tabs for centrifuge and flotation
        tab1, tab2 = st.tabs(["Basket Centrifuge", "Froth Flotation"])
        
        with tab1:
            basket_centrifuge.app()
        
        with tab2:
            froth_flotation.app()
    elif selected_experiment == "7. Rotary Vacuum Filter":
        rotary_vacuum_filter.app()
    elif selected_experiment == "9. Classifiers":
        classifiers.app()
    else:
        st.info(f"Report generation for {selected_experiment} is not yet implemented.")
        st.write("Currently, report generation is available for the following experiments:")
        st.write("- Experiment 7: Rotary Vacuum Filter")
        st.write("- Experiment 8: Centrifuge and Flotation")
        st.write("- Experiment 9: Classifiers")