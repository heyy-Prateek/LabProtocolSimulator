"""
Main application module for Chemical Engineering Lab Simulator.
"""

import streamlit as st
import platform
import os

# Detect if running on Android or mobile
is_mobile = False
user_agent = os.environ.get('HTTP_USER_AGENT', '').lower()
if 'android' in user_agent or 'mobile' in user_agent or platform.system() == "Android":
    is_mobile = True
    
# Set page configuration based on device type
st.set_page_config(
    page_title="Chemical Engineering Lab Simulator",
    page_icon="🧪",
    layout="wide" if not is_mobile else "centered"
)

def main():
    # App title as the main header, centered
    st.markdown("<h1 style='text-align: center;'>Chemical Engineering Laboratory Simulator</h1>", unsafe_allow_html=True)
    
    st.sidebar.title("Experiment Selection")
    
    # Add mode options in sidebar
    view_mode = st.sidebar.radio("Mode", ["Simulation", "Demo Video", "Quiz", "Report Generation", "Chat Assistant"])
    
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
    
    # Store current experiment in session state for reference by other modules
    st.session_state['selected_experiment'] = experiment
    
    # Common experiment name mapping
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
    
    # Display the appropriate experiment page based on selection
    if experiment == "Home":
        display_home_page()
    elif view_mode == "Chat Assistant":
        try:
            # Import chat module and display chat interface
            from chemengsim import chat
            chat.chat_interface()
        except Exception as e:
            st.error(f"Error loading chat assistant: {str(e)}")
            st.info("The chat assistant feature may still be under development.")
    elif view_mode == "Quiz":
        try:
            # Extract experiment name from selection
            exp_num = int(experiment.split(".")[0])
            
            # Import quiz module and run quiz
            from chemengsim.quizzes import quiz_module
            quiz_module.run_quiz(exp_names[exp_num])
        except Exception as e:
            st.error(f"Error loading quiz: {str(e)}")
            st.info("Some quizzes may still be under development.")
    elif view_mode == "Demo Video":
        try:
            # Skip if Home is selected
            if experiment != "Home":
                # Extract experiment name from selection
                exp_num = int(experiment.split(".")[0])
                
                # Import demo video module and display video
                from chemengsim.videos import demo_videos
                demo_videos.display_demo_video(exp_names[exp_num])
            else:
                st.title("Demonstration Videos")
                st.markdown("""
                Select an experiment from the sidebar to view its demonstration video.
                
                These videos show the actual laboratory procedures and equipment operation
                for each experiment in the Chemical Engineering Laboratory.
                """)
                st.info("Please select an experiment from the sidebar to view its demonstration video.")
        except Exception as e:
            st.error(f"Error loading demonstration video: {str(e)}")
            st.info("Some demonstration videos may still be under development.")
    elif view_mode == "Report Generation":
        # Import and run the report generation module
        try:
            from chemengsim.report_generation import main as report_main
            report_main.main()
        except Exception as e:
            st.error(f"Error loading report generation module: {str(e)}")
            st.info("The report generation feature may still be under development for some experiments.")
    else:  # Simulation mode
        if experiment != "Home":
            # Extract experiment name from selection for import
            exp_num = int(experiment.split(".")[0])
            
            try:
                # Dynamic import of the experiment module
                module_name = f"chemengsim.experiments.{exp_names[exp_num]}"
                module = __import__(module_name, fromlist=['app'])
                module.app()
            except Exception as e:
                st.error(f"Error loading experiment simulation: {str(e)}")
                st.write(f"## {experiment}")
                st.write("### What you'll learn in this experiment:")
            
            if experiment == "1. Isothermal Batch Reactor":
                st.write("""
                - How concentration changes with time in a batch reactor
                - Effect of reaction rate constant on conversion
                - Calculation of residence time and space-time
                - Analysis of reaction kinetics
                """)
                
            elif experiment == "2. Isothermal Semi-batch Reactor":
                st.write("""
                - How feed rate affects reaction progress
                - Material balances in semi-batch operation
                - Comparison with batch reactor performance
                - Effect of feeding policies on conversion
                """)
                
            elif experiment == "3. Isothermal CSTR":
                st.write("""
                - Steady-state operation of continuous reactors
                - Effect of residence time on conversion
                - Multiple steady states and stability
                - Comparison with other reactor types
                """)
                
            elif experiment == "4. Isothermal PFR":
                st.write("""
                - Plug flow behavior and its assumptions
                - Concentration profiles along reactor length
                - Conversion as a function of residence time
                - Comparison with CSTR performance
                """)
                
            elif experiment == "5. Crushers and Ball Mill":
                st.write("""
                - Size reduction principles
                - Energy requirements for crushing
                - Product size distribution analysis
                - Performance metrics for crushers
                """)
                
            elif experiment == "6. Plate and Frame Filter Press":
                st.write("""
                - Solid-liquid separation theory
                - Cake filtration fundamentals
                - Constant pressure vs. constant rate filtration
                - Determination of filter medium resistance
                """)
                
            elif experiment == "7. Rotary Vacuum Filter":
                st.write("""
                - Continuous filtration principles
                - Drum operation zones and timing
                - Effect of vacuum level on filtration rate
                - Cake washing and dewatering
                """)
                
            elif experiment == "8. Centrifuge and Flotation":
                st.write("""
                - Centrifugal separation principles
                - Effect of G-force on separation efficiency
                - Flotation chemistry and surface properties
                - Froth stability and collection mechanisms
                """)
                
            elif experiment == "9. Classifiers":
                st.write("""
                - Hydraulic classification principles
                - Settling of particles in fluids
                - Cut size and separation efficiency
                - Thickener design and operation
                """)
                
            elif experiment == "10. Trommel":
                st.write("""
                - Screening principles and equipment
                - Effect of operating parameters on screening efficiency
                - Size distribution analysis
                - Screen capacity and limitations
                """)
            
            st.markdown("---")
            if view_mode == "Simulation":
                st.info("Please check the Quiz mode to test your knowledge or the Report Generation mode to create a lab report for this experiment!")

    # Add footer to all pages
    st.markdown("---")
    
    # Footer text only
    st.markdown("""
    <div style='text-align: center;'>
        <p>© 2025 Chemical Engineering Laboratory Simulator | Created by Prateek Saxena</p>
        <p>BITS Pilani, India | Contact: +91 9458827686</p>
        <p>MADE WITH LOVE FOR CHEMICAL ENGINEERING COMMUNITY ❤️</p>
    </div>
    """, unsafe_allow_html=True)

def display_home_page():
    """Display the enhanced home page with experiment cards"""
    
    # Detect if running on mobile
    global is_mobile
    
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
    /* Mobile-specific styles */
    @media (max-width: 768px) {
        .experiment-card {
            padding: 15px;
            margin-bottom: 15px;
        }
        .experiment-title {
            font-size: 16px;
        }
        h1 {
            font-size: 1.5rem !important;
        }
        h3 {
            font-size: 1.1rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header section - simplified since we have the logo in the main header
    st.markdown("<h1 style='text-align: center;'>Welcome to the Chemical Engineering Laboratory Simulator</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Introduction
    st.markdown("""
    ### 🧪 About the Simulator
    
    This application allows you to explore and simulate 10 different chemical engineering experiments
    without the constraints of physical laboratory settings. You can:
    
    - Adjust experimental parameters and see real-time results
    - Visualize data through interactive plots and graphs
    - Watch demonstration videos of actual laboratory procedures
    - Download simulation data for further analysis
    - Test your knowledge with quiz mode for each experiment
    - Generate professional lab reports by entering observation data
    
    Select an experiment from the sidebar and choose a mode to begin exploring.
    """)
    
    st.success("Simulation, demo video, quiz, and report generation modes are all available! Select an experiment from the sidebar to begin.")
    
    st.markdown("---")
    
    # Display experiment cards in a grid layout appropriate for the device
    st.markdown("### Available Experiments")
    
    # Use 1 column for mobile or 2 columns for desktop
    if is_mobile:
        # Mobile layout - single column
        experiments = [
            ("1. Isothermal Batch Reactor", "Study of a non-catalytic homogeneous reaction in a batch reactor, including concentration profiles and conversion analysis."),
            ("2. Isothermal Semi-batch Reactor", "Simulation of reactions in semi-batch mode with continuous addition of one reactant."),
            ("3. Isothermal CSTR", "Continuous stirred tank reactor simulation with heat transfer analysis."),
            ("4. Isothermal PFR", "Plug flow reactor with variable parameters and comparison to other reactor types."),
            ("5. Crushers and Ball Mill", "Size reduction equipment simulation and analysis of product size distribution."),
            ("6. Plate and Frame Filter Press", "Solid-liquid separation with analysis of filtration rates and cake formation."),
            ("7. Rotary Vacuum Filter", "Continuous filtration process with drum operation visualization."),
            ("8. Centrifuge and Flotation", "Solid-liquid separation in basket centrifuge and mineral separation in flotation cells."),
            ("9. Classifiers", "Particle classification using cone classifiers and thickeners for solid-liquid separation."),
            ("10. Trommel", "Rotary screen simulation with particle size distribution and efficiency analysis.")
        ]
        
        for title, description in experiments:
            st.markdown(f"""
            <div class="experiment-card">
                <p class="experiment-title">{title}</p>
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        # Desktop layout - two columns
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