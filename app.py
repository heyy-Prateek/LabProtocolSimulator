import streamlit as st

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
    
    # Add quiz mode option in sidebar
    view_mode = st.sidebar.radio("Mode", ["Simulation", "Quiz"])
    
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
        display_home_page()
    elif view_mode == "Quiz":
        try:
            # Extract experiment name from selection
            exp_num = int(experiment.split(".")[0])
            exp_names = [
                "",  # Home page has no number
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
            
            # Import quiz module and run quiz
            from quizzes import quiz_module
            quiz_module.run_quiz(exp_names[exp_num])
        except Exception as e:
            st.error(f"Error loading quiz: {str(e)}")
            st.info("Some quizzes may still be under development.")
    else:
        try:
            # Load the appropriate experiment module
            if experiment == "1. Isothermal Batch Reactor":
                from experiments import batch_reactor
                batch_reactor.app()
            elif experiment == "2. Isothermal Semi-batch Reactor":
                from experiments import semi_batch_reactor
                semi_batch_reactor.app()
            elif experiment == "3. Isothermal CSTR":
                from experiments import cstr
                cstr.app()
            elif experiment == "4. Isothermal PFR":
                from experiments import pfr
                pfr.app()
            elif experiment == "5. Crushers and Ball Mill":
                from experiments import crushers
                crushers.app()
            elif experiment == "6. Plate and Frame Filter Press":
                from experiments import filter_press
                filter_press.app()
            elif experiment == "7. Rotary Vacuum Filter":
                from experiments import rotary_vacuum_filter
                rotary_vacuum_filter.app()
            elif experiment == "8. Centrifuge and Flotation":
                from experiments import centrifuge_flotation
                centrifuge_flotation.app()
            elif experiment == "9. Classifiers":
                from experiments import classifiers
                classifiers.app()
            elif experiment == "10. Trommel":
                from experiments import trommel
                trommel.app()
        except Exception as e:
            st.error(f"Error loading experiment: {str(e)}")
            st.warning("The experiment modules are still being set up. Please check back soon!")

def display_home_page():
    """Display the enhanced home page with experiment cards"""
    
    # Basic styling for the cards
    st.markdown("""
    <style>
    .experiment-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .experiment-title {
        color: #1E88E5;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header section
    st.image("generated-icon.png", width=150)
    st.markdown("<h1 style='text-align: center;'>Chemical Engineering Laboratory Simulator</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Virtual Laboratory for Chemical Engineering Students</h3>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Introduction
    st.markdown("""
    ### 🧪 Welcome to the Chemical Engineering Laboratory Simulator
    
    This application allows you to explore and simulate 10 different chemical engineering experiments
    without the constraints of physical laboratory settings. You can:
    
    - Adjust experimental parameters and see real-time results
    - Visualize data through interactive plots and graphs
    - Download simulation data for further analysis
    - Test your knowledge with quiz mode for each experiment
    
    Select an experiment from the sidebar or browse the available experiments below.
    """)
    
    st.markdown("---")
    
    # Display experiment cards in a grid
    st.markdown("### Available Experiments")
    
    # Create a 2-column layout
    col1, col2 = st.columns(2)
    
    # Experiments in first column
    with col1:
        st.markdown("""
        <div class="experiment-card">
            <p class="experiment-title">1. Isothermal Batch Reactor</p>
            <p>Study of a non-catalytic homogeneous reaction in a batch reactor, including concentration profiles and conversion analysis.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="experiment-card">
            <p class="experiment-title">2. Isothermal Semi-batch Reactor</p>
            <p>Simulation of reactions in semi-batch mode with continuous addition of one reactant.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="experiment-card">
            <p class="experiment-title">3. Isothermal CSTR</p>
            <p>Continuous stirred tank reactor simulation with heat transfer analysis.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="experiment-card">
            <p class="experiment-title">4. Isothermal PFR</p>
            <p>Plug flow reactor with variable parameters and comparison to other reactor types.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="experiment-card">
            <p class="experiment-title">5. Crushers and Ball Mill</p>
            <p>Size reduction equipment simulation and analysis of product size distribution.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Experiments in second column
    with col2:
        st.markdown("""
        <div class="experiment-card">
            <p class="experiment-title">6. Plate and Frame Filter Press</p>
            <p>Solid-liquid separation with analysis of filtration rates and cake formation.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="experiment-card">
            <p class="experiment-title">7. Rotary Vacuum Filter</p>
            <p>Continuous filtration process with drum operation visualization.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="experiment-card">
            <p class="experiment-title">8. Centrifuge and Flotation</p>
            <p>Solid-liquid separation in basket centrifuge and mineral separation in flotation cells.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="experiment-card">
            <p class="experiment-title">9. Classifiers</p>
            <p>Particle classification using cone classifiers and thickeners for solid-liquid separation.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="experiment-card">
            <p class="experiment-title">10. Trommel</p>
            <p>Rotary screen simulation with particle size distribution and efficiency analysis.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center;'>
        <p>© 2025 Chemical Engineering Laboratory Simulator | Created with ❤️ for Chemical Engineering Students</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
