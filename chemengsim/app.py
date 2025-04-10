"""
Main application module for Chemical Engineering Lab Simulator.
"""

import streamlit as st
import platform
import os
import numpy as np
import pandas as pd
import base64
from io import BytesIO
import streamlit.components.v1 as components
import math
import sys

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

# Function to show the welcome page
def show_welcome_page():
    # Custom CSS for the welcome page
    st.markdown("""
    <style>
    .welcome-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 50px 20px;
        text-align: center;
    }
    .welcome-header {
        color: #2E86C1;
        font-size: 2.5rem;
        margin-bottom: 30px;
    }
    .welcome-subheader {
        color: #5D6D7E;
        font-size: 1.3rem;
        margin-bottom: 50px;
    }
    .ui-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 15px;
        width: 100%;
        max-width: 350px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .ui-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .ui-card-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .ui-card-image {
        width: 100%;
        height: 200px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 5px;
        overflow: hidden;
    }
    .ui-card-image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .ui-card-description {
        color: #495057;
        margin-bottom: 20px;
    }
    .ui-button {
        background-color: #2E86C1;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .ui-button:hover {
        background-color: #1A5276;
    }
    .ui-card-dark {
        background-color: #1E1E1E;
        color: #E0E0E0;
    }
    .ui-card-dark .ui-card-title {
        color: #FFFFFF;
    }
    .ui-card-dark .ui-card-description {
        color: #B0B0B0;
    }
    .ui-card-dark .ui-card-image {
        background-color: #2D2D2D;
    }
    .ui-button-dark {
        background-color: #3700B3;
    }
    .ui-button-dark:hover {
        background-color: #6200EE;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Welcome content with actual preview images
    st.markdown("""
    <div class="welcome-container">
        <h1 class="welcome-header">Welcome to Chemical Engineering Lab Simulator</h1>
        <p class="welcome-subheader">Choose your preferred interface to get started</p>
        
        <div style="display: flex; flex-wrap: wrap; justify-content: center;">
            <!-- Classic UI Card -->
            <div class="ui-card">
                <div class="ui-card-title">Classic UI</div>
                <div class="ui-card-image">
                    <img src="data:image/png;base64,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" alt="Classic Interface Preview">
                <div class="ui-card-image">Classic Interface Preview</div>
                <div class="ui-card-description">
                    The original interface with sidebar navigation and traditional layout. 
                    Best for educational purposes with clear structure.
                </div>
                <button class="ui-button" onclick="document.getElementById('classic-ui-button').click();">
                    Select Classic UI
                </button>
            </div>
            
            <!-- Minimalist Dark UI Card -->
            <div class="ui-card ui-card-dark">
                <div class="ui-card-title">Minimalist Dark UI</div>
                <div class="ui-card-image">Modern Interface Preview</div>
                <div class="ui-card-description">
                    A modern, Apple-inspired dark interface with sleek animations and 
                    minimalist design. More immersive experience.
                </div>
                <button class="ui-button ui-button-dark" onclick="document.getElementById('dark-ui-button').click();">
                    Select Dark UI
                </button>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hidden buttons that will be triggered by the HTML buttons
    if st.button("Select Classic UI", key="classic-ui-button", type="primary"):
        st.session_state['ui_version'] = "classic"
        st.rerun()
        
    if st.button("Select Dark UI", key="dark-ui-button", type="primary"):
        st.session_state['ui_version'] = "dark"
        st.rerun()

# Custom CSS for top left corner buttons
st.markdown("""
<style>
.top-navbar {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 999;
    width: auto;
    padding: 8px;
    display: flex;
    gap: 8px;
}
.nav-button {
    background-color: #2196F3;
    color: white;
    padding: 8px 12px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 14px;
    margin: 4px 2px;
    cursor: pointer;
    border: none;
    border-radius: 4px;
}
.nav-button:hover {
    background-color: #0b7dda;
}
/* Pushes streamlit content down to make room for navbar */
.main .block-container {
    padding-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# Python-based calculator implementation inspired by the GitHub repo
class Calculator:
    def __init__(self):
        self.expression = ""
        self.memory = 0
        self.result = 0
        
    def append_value(self, value):
        self.expression += value
        return self.expression
        
    def clear_entry(self):
        if self.expression:
            self.expression = self.expression[:-1]
        return self.expression
        
    def clear_all(self):
        self.expression = ""
        return self.expression
        
    def toggle_sign(self):
        if self.expression:
            if self.expression.startswith('-'):
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression
        return self.expression
        
    def mem_clear(self):
        self.memory = 0
        return self.expression
        
    def mem_recall(self):
        self.expression += str(self.memory)
        return self.expression
        
    def mem_add(self):
        try:
            self.calculate()
            self.memory += float(self.result)
            return self.expression
        except:
            return "Error"
        
    def mem_subtract(self):
        try:
            self.calculate()
            self.memory -= float(self.result)
            return self.expression
        except:
            return "Error"
        
    def factorial(self):
        try:
            n = int(float(self.expression))
            if n >= 0:
                self.result = math.factorial(n)
                self.expression = str(self.result)
                return self.expression
            else:
                return "Error"
        except:
            return "Error"
        
    def calculate(self):
        if not self.expression:
            return "0"
        
        try:
            # Replace math symbols with Python equivalents
            expr = self.expression
            expr = expr.replace('π', str(math.pi))
            expr = expr.replace('e', str(math.e))
            expr = expr.replace('sin(', 'math.sin(')
            expr = expr.replace('cos(', 'math.cos(')
            expr = expr.replace('tan(', 'math.tan(')
            expr = expr.replace('log(', 'math.log10(')
            expr = expr.replace('ln(', 'math.log(')
            expr = expr.replace('√(', 'math.sqrt(')
            expr = expr.replace('^', '**')
            
            # Evaluate the expression
            self.result = eval(expr)
            self.expression = str(self.result)
            return self.expression
        except Exception as e:
            return "Error"

def scientific_calculator_ui():
    """Display a scientific calculator UI in Streamlit"""
    if 'calculator' not in st.session_state:
        st.session_state.calculator = Calculator()
    
    calc = st.session_state.calculator
    
    # Display area
    display = st.text_input("", value=calc.expression or "0", key="calc_display", disabled=True)
    
    # Create button layout
    rows = [
        # First Row
        ["MC", "MR", "M+", "M-", "C"],
        # Second Row
        ["sin", "cos", "tan", "x!", "CE"],
        # Third Row
        ["log", "ln", "^", "√", "/"],
        # Fourth Row
        ["π", "7", "8", "9", "×"],
        # Fifth Row
        ["e", "4", "5", "6", "-"],
        # Sixth Row
        ["±", "1", "2", "3", "+"],
        # Seventh Row
        ["(", ")", "0", ".", "="]
    ]
    
    # Style for different button types
    button_styles = {
        "default": {"background-color": "#f8f9fa", "color": "#212529"},
        "function": {"background-color": "#e9ecef", "color": "#495057"},
        "operator": {"background-color": "#dee2e6", "color": "#495057"},
        "memory": {"background-color": "#ffebcd", "color": "#212529"},
        "equal": {"background-color": "#4d90fe", "color": "#ffffff"}
    }
    
    # Button actions
    button_actions = {
        "MC": calc.mem_clear,
        "MR": calc.mem_recall,
        "M+": calc.mem_add,
        "M-": calc.mem_subtract,
        "C": calc.clear_all,
        "CE": calc.clear_entry,
        "sin": lambda: calc.append_value("sin("),
        "cos": lambda: calc.append_value("cos("),
        "tan": lambda: calc.append_value("tan("),
        "x!": calc.factorial,
        "log": lambda: calc.append_value("log("),
        "ln": lambda: calc.append_value("ln("),
        "^": lambda: calc.append_value("^"),
        "√": lambda: calc.append_value("√("),
        "π": lambda: calc.append_value("π"),
        "e": lambda: calc.append_value("e"),
        "±": calc.toggle_sign,
        "(": lambda: calc.append_value("("),
        ")": lambda: calc.append_value(")"),
        "/": lambda: calc.append_value("/"),
        "×": lambda: calc.append_value("*"),
        "-": lambda: calc.append_value("-"),
        "+": lambda: calc.append_value("+"),
        "=": calc.calculate,
        "0": lambda: calc.append_value("0"),
        "1": lambda: calc.append_value("1"),
        "2": lambda: calc.append_value("2"),
        "3": lambda: calc.append_value("3"),
        "4": lambda: calc.append_value("4"),
        "5": lambda: calc.append_value("5"),
        "6": lambda: calc.append_value("6"),
        "7": lambda: calc.append_value("7"),
        "8": lambda: calc.append_value("8"),
        "9": lambda: calc.append_value("9"),
        ".": lambda: calc.append_value(".")
    }
    
    # Button style mapping
    button_style_map = {
        "MC": "memory", "MR": "memory", "M+": "memory", "M-": "memory",
        "C": "function", "CE": "function",
        "sin": "function", "cos": "function", "tan": "function",
        "log": "function", "ln": "function", "^": "function", "√": "function",
        "x!": "function", "π": "function", "e": "function", "±": "function",
        "(": "function", ")": "function",
        "/": "operator", "×": "operator", "-": "operator", "+": "operator",
        "=": "equal"
    }
    
    # Create calculator grid using columns
    for row in rows:
        cols = st.columns(5)
        for i, button_text in enumerate(row):
            style = button_style_map.get(button_text, "default")
            button_style = button_styles[style]
            
            # Create button with proper style
            if cols[i].button(button_text, key=f"calc_{button_text}", 
                           use_container_width=True):
                action = button_actions.get(button_text)
                if action:
                    result = action()
                    # Update display
                    st.session_state.calculator.expression = result
                    st.rerun()

# Create a home button function that redirects to home
def go_home():
    st.session_state['selected_experiment'] = "Home"
    # Reset any other state as needed
    if 'view_mode' in st.session_state:
        st.session_state['view_mode'] = "Simulation"
    # Use st.rerun() instead of experimental_rerun
    st.rerun()

def main():
    # Check if UI version has been selected
    if 'ui_version' not in st.session_state:
        # If not selected, show the welcome page
        show_welcome_page()
        return
    
    # UI version has been selected, continue with the appropriate version
    ui_version = st.session_state['ui_version']
    
    if ui_version == "dark":
        # Placeholder for dark UI implementation
        st.write("Dark UI version coming soon! For now, using Classic UI.")
        st.session_state['ui_version'] = "classic"
        st.rerun()
    
    # Continue with classic UI implementation
    # Title
    st.title("Chemical Engineering Laboratory Simulator")
    
    st.markdown("""
    This application simulates experiments from the Chemical Engineering Laboratory-II course.
    Select an experiment from the sidebar to begin.
    """)
    
    st.sidebar.title("Experiment Selection")
    
    # Add a home button at the top of the sidebar that's always visible
    if st.sidebar.button("🏠", use_container_width=True):
        st.session_state['selected_experiment'] = "Home"
        st.session_state['view_mode'] = "Simulation"
        st.rerun()
    
    # Add a chat button (icon only)
    if st.sidebar.button("💬", key="chat_button", use_container_width=True):
        # Always directly set mode to Chat Assistant and force a rerun
        st.session_state['view_mode'] = "Chat Assistant"
        # No need to change experiment selection
        st.rerun()
    
    # Add UI switch button
    if st.sidebar.button("🔄 Switch UI", key="switch_ui"):
        # Remove UI preference and go back to selection
        st.session_state.pop('ui_version', None)
        st.rerun()
    
    # Add a horizontal rule for visual separation
    st.sidebar.markdown("---")
    
    # For tracking if selections have changed
    current_mode = st.session_state.get('view_mode', "Simulation")
    current_experiment = st.session_state.get('selected_experiment', "Home")
    
    # Add mode options in sidebar (excluding Chat Assistant which has its own checkbox)
    view_mode = st.sidebar.radio("Mode", ["Simulation", "Demo Video", "Quiz", "Report Generation"])
    
    # Store temporary mode selection (will be committed on submit)
    temp_mode = view_mode
    
    # Add experiment selection
    temp_experiment = st.sidebar.selectbox(
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
    
    # Add submit button to confirm selection
    if st.sidebar.button("Submit Selection", type="primary", use_container_width=True):
        # Update session state with new selections
        st.session_state['selected_experiment'] = temp_experiment
        st.session_state['view_mode'] = temp_mode
        st.rerun()
    
    # Get selected experiment and mode from session state
    experiment = st.session_state.get('selected_experiment', "Home")
    view_mode = st.session_state.get('view_mode', "Simulation")
    
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
    
    # Header section
    try:
        st.image("generated-icon.png", width=100 if is_mobile else 150)
    except:
        st.write("## 🧪 Chemical Engineering Laboratory Simulator")
    
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
    - Watch demonstration videos of actual laboratory procedures
    - Download simulation data for further analysis
    - Test your knowledge with quiz mode for each experiment
    - Generate professional lab reports by entering observation data
    - Get instant answers to chemical engineering questions with the Chat Assistant
    
    Select an experiment from the sidebar and choose a mode to begin exploring.
    """)
    
    st.success("Simulation, demo video, quiz, report generation, and chat assistant modes are all available! Select an experiment from the sidebar to begin.")
    
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
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center;'>
        <p>© 2025 Chemical Engineering Laboratory Simulator | Created by Prateek Saxena</p>
        <p>BITS Pilani, India | Contact: +91 9458827686</p>
        <p>MADE WITH LOVE FOR CHEMICAL ENGINEERING COMMUNITY ❤️</p>
    </div>
    """, unsafe_allow_html=True)