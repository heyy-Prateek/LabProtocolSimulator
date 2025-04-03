import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from experiments import (
    batch_reactor, 
    semi_batch_reactor, 
    cstr, 
    pfr, 
    crushers, 
    filter_press, 
    rotary_vacuum_filter,
    centrifuge_flotation,
    classifiers,
    trommel
)

st.set_page_config(
    page_title="Chemical Engineering Lab Simulator",
    page_icon="🧪",
    layout="wide"
)

def main():
    st.title("Chemical Engineering Laboratory Simulator")
    st.markdown("""
    This application simulates experiments from the Chemical Engineering Laboratory-II course.
    Select an experiment from the sidebar to begin.
    """)
    
    st.sidebar.title("Experiment Selection")
    experiment = st.sidebar.selectbox(
        "Choose an experiment",
        [
            "Home",
            "1. Isothermal Batch Reactor",
            "2. Isothermal Semi-batch Reactor",
            "3. Isothermal CSTR",
            "4. Isothermal PFR",
            "5. Crushers and Ball Mill",
            "6. Plate and Frame Filter Press",
            "7. Rotary Vacuum Filter",
            "8. Centrifuge and Flotation",
            "9. Classifiers",
            "10. Trommel"
        ]
    )
    
    # Display the appropriate experiment page based on selection
    if experiment == "Home":
        st.image("https://upload.wikimedia.org/wikipedia/en/c/c9/BITS_Pilani-Logo.svg", width=300)
        st.write("### Department of Chemical Engineering, BITS Pilani")
        st.write("#### Chemical Engineering Laboratory – II (Cycle – I)")
        
        st.markdown("""
        Welcome to the Chemical Engineering Laboratory Simulator. This application allows you to:
        
        - Adjust experimental parameters
        - Simulate reactions and processes
        - Visualize results with graphs and data tables
        - Understand theoretical concepts
        
        Select an experiment from the sidebar to get started.
        """)
        
        st.markdown("---")
        st.write("### Available Experiments:")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("1. Isothermal Batch Reactor")
            st.write("2. Isothermal Semi-batch Reactor")
            st.write("3. Isothermal CSTR")
            st.write("4. Isothermal PFR")
            st.write("5. Crushers and Ball Mill")
            
        with col2:
            st.write("6. Plate and Frame Filter Press")
            st.write("7. Rotary Vacuum Filter")
            st.write("8. Centrifuge and Flotation")
            st.write("9. Classifiers")
            st.write("10. Trommel")
    
    elif experiment == "1. Isothermal Batch Reactor":
        batch_reactor.app()
    
    elif experiment == "2. Isothermal Semi-batch Reactor":
        semi_batch_reactor.app()
    
    elif experiment == "3. Isothermal CSTR":
        cstr.app()
    
    elif experiment == "4. Isothermal PFR":
        pfr.app()
    
    elif experiment == "5. Crushers and Ball Mill":
        crushers.app()
    
    elif experiment == "6. Plate and Frame Filter Press":
        filter_press.app()
    
    elif experiment == "7. Rotary Vacuum Filter":
        rotary_vacuum_filter.app()
    
    elif experiment == "8. Centrifuge and Flotation":
        centrifuge_flotation.app()
    
    elif experiment == "9. Classifiers":
        classifiers.app()
    
    elif experiment == "10. Trommel":
        trommel.app()

if __name__ == "__main__":
    main()
