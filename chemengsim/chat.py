"""
Chat Assistant Module for Chemical Engineering Laboratory Simulator.
This module implements a chat interface where users can ask questions related to
chemical engineering concepts and experiments.
"""

import streamlit as st
import os
import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime
import sys
import importlib
import subprocess
import math
import re


def check_dependencies():
    """
    Check if required packages are installed and install if necessary.
    """
    required_packages = {
        'requests': 'requests'
    }
    
    missing_packages = []
    
    for package, import_name in required_packages.items():
        try:
            importlib.import_module(import_name)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        st.warning(f"Missing required packages: {', '.join(missing_packages)}")
        
        if st.button("Install Missing Packages"):
            with st.spinner("Installing packages..."):
                for package in missing_packages:
                    try:
                        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                        st.success(f"Successfully installed {package}")
                    except Exception as e:
                        st.error(f"Failed to install {package}: {str(e)}")
            
            st.info("Installation complete. Please refresh the page.")
            st.stop()


def chat_interface():
    """
    Displays a chat interface that allows users to ask questions about 
    chemical engineering concepts and experiments.
    """
    # Check for required dependencies
    check_dependencies()
    
    # Custom CSS styling for chat interface
    st.markdown("""
    <style>
    .chat-header {
        color: #2E86C1;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .chat-subheader {
        color: #2E86C1;
        font-weight: bold;
        margin-top: 1.5rem;
        border-bottom: 1px solid #2E86C1;
        padding-bottom: 0.5rem;
    }
    .chat-message-user {
        background-color: #E8F4FD;
        border-radius: 10px;
        padding: 10px 15px;
        margin: 5px 0;
    }
    .chat-message-assistant {
        background-color: #F0F2F6;
        border-radius: 10px;
        padding: 10px 15px;
        margin: 5px 0;
    }
    .clear-button {
        background-color: #FF6B6B;
        color: white;
        border-radius: 5px;
        padding: 5px 10px;
        border: none;
        cursor: pointer;
    }
    .clear-button:hover {
        background-color: #FF4949;
    }
    .stButton>button {
        background-color: #FF6B6B;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FF4949;
    }
    .stTextInput>div>div>input {
        background-color: #F8F9FA;
        border: 1px solid #CED4DA;
        border-radius: 5px;
    }
    .api-key-section {
        background-color: #F8F9FA;
        border-radius: 5px;
        padding: 15px;
        margin: 10px 0;
        border: 1px solid #E6E6E6;
    }
    .source-tag {
        font-size: 0.7rem;
        color: #6c757d;
        text-align: right;
        font-style: italic;
        margin-top: 5px;
    }
    .toggle-section {
        background-color: #F0F2F6;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 15px;
        border: 1px solid #E6E6E6;
    }
    /* Hide container padding on input elements - makes bars less prominent */
    div[data-baseweb="input"] {
        background-color: transparent !important;
    }
    /* Hide other input fields except API token */
    .main-chat-input {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Title with custom CSS class
    st.markdown("<h1 class='chat-header'>Chemical Engineering Chat Assistant</h1>", unsafe_allow_html=True)
    
    # Introduction and instructions
    st.markdown("""
    Welcome to the Chemical Engineering Chat Assistant! Ask questions about:
    
    - Chemical engineering concepts
    - Laboratory procedures
    - Experimental calculations
    - Interpretation of results
    - Troubleshooting experiments
    """)
    
    # Simple toggle for API mode
    if "use_api" not in st.session_state:
        st.session_state.use_api = False  # Default to offline mode
    
    # API toggle
    use_api = st.toggle("Use External API for Advanced Questions", value=st.session_state.use_api)
    st.session_state.use_api = use_api
    
    # Show appropriate message based on API mode
    if use_api:
        st.info("External API mode enabled. The assistant will attempt to answer more specialized questions.")
    else:
        st.info("Using built-in knowledge only. For more advanced questions, enable the API feature.")
    
    # Handle API token in session state (backend)
    if "huggingface_api_token" not in st.session_state:
        st.session_state.huggingface_api_token = ""
    
    # Model selection in session state (backend)
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = "google/flan-t5-xxl"
    
    # API settings - hide in expander to keep it out of the way
    if st.session_state.use_api:
        with st.expander("API Settings", expanded=False):
            # API key input
            api_key_input = st.text_input(
                "Enter your Hugging Face API Token:",
                type="password",
                value=st.session_state.huggingface_api_token,
                key="api_key_input"
            )
            
            # Save API key to session state
            if api_key_input:
                st.session_state.huggingface_api_token = api_key_input
                st.success("API Token saved for this session")
                
            st.markdown("""
            You can get a free API token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
            """)
    
    # Initialize chat history in session state if it doesn't exist
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        
    # Clear chat button
    col1, col2 = st.columns([5, 1])
    with col2:
        if st.button("Clear Chat", key="clear_chat"):
            st.session_state.chat_history = []
            st.rerun()
    
    # Chat input
    user_input = st.chat_input("Ask a question about chemical engineering...")
    
    # Process user input when submitted
    if user_input:
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Generate response based on whether API is enabled
        if st.session_state.use_api:
            response, source = generate_response_with_api(user_input, st.session_state.huggingface_api_token)
        else:
            response, source = generate_response_builtin(user_input)
        
        # Add assistant response to chat history with source info
        st.session_state.chat_history.append({"role": "assistant", "content": response, "source": source})
        
        # Refresh the UI to show updated chat
        st.rerun()
    
    # Horizontal line to separate input from history
    st.markdown("---")
    
    # Display chat history header
    if len(st.session_state.chat_history) > 0:
        st.markdown("<h2 class='chat-subheader'>Conversation History</h2>", unsafe_allow_html=True)
    
    # Display chat history with custom styling
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message["role"] == "assistant" and "source" in message:
                st.markdown(f"<p class='source-tag'>Source: {message['source']}</p>", unsafe_allow_html=True)


def math_calculator(expression):
    """
    Evaluates mathematical expressions and returns the result.
    
    Args:
        expression (str): The mathematical expression to evaluate
        
    Returns:
        tuple: (result_text, success) - The result text and boolean indicating success
    """
    try:
        # Clean up the expression
        # Remove "calculate", "compute", "what is", etc.
        cleaned = expression.lower()
        prefixes = ["calculate", "compute", "what is", "what's", "solve", "evaluate"]
        for prefix in prefixes:
            if cleaned.startswith(prefix):
                cleaned = cleaned[len(prefix):].strip()
        
        # Remove question marks and other punctuation at the end
        cleaned = cleaned.rstrip('?.,;!')
        
        # Check if it looks like a math expression
        # Pattern to match common math operations
        math_pattern = r'[\d\s\+\-\*\/\^\(\)\.\,\%\=\<\>π√sin|cos|tan|log|ln]+'
        if not re.match(math_pattern, cleaned):
            return None, False
        
        # Replace math symbols with Python equivalents
        expr = cleaned
        expr = expr.replace('π', str(math.pi))
        expr = expr.replace('pi', str(math.pi))
        expr = expr.replace('e', str(math.e))
        expr = expr.replace('sin(', 'math.sin(')
        expr = expr.replace('cos(', 'math.cos(')
        expr = expr.replace('tan(', 'math.tan(')
        expr = expr.replace('log(', 'math.log10(')
        expr = expr.replace('ln(', 'math.log(')
        expr = expr.replace('√(', 'math.sqrt(')
        expr = expr.replace('sqrt(', 'math.sqrt(')
        expr = expr.replace('^', '**')
        
        # Special handling for percentages
        expr = expr.replace('%', '/100')
        
        # Special handling for factorial
        if 'factorial(' in expr or 'fact(' in expr:
            expr = expr.replace('factorial(', 'math.factorial(')
            expr = expr.replace('fact(', 'math.factorial(')
        
        # Evaluate the expression
        result = eval(expr)
        
        # Format the result for display
        if isinstance(result, float):
            # Check if it's close to an integer
            if abs(result - round(result)) < 1e-10:
                result = int(round(result))
            else:
                # Display with appropriate precision
                result = round(result, 10)
                # Remove trailing zeros
                result = str(result).rstrip('0').rstrip('.') if '.' in str(result) else str(result)
        
        return f"""
        ### Mathematical Calculation
        
        Expression: `{cleaned}`
        
        Result: **{result}**
        """, True
        
    except Exception as e:
        # Not a valid math expression or error in evaluation
        return None, False


def generate_response_builtin(question):
    """
    Generates a response based on the user's question using only built-in knowledge.
    
    Args:
        question (str): The user's question
        
    Returns:
        tuple: (response_text, source) - The response text and its source
    """
    # First, check if it's a math calculation
    math_result, is_math = math_calculator(question)
    if is_math:
        return math_result, "Calculator"
    
    # Default responses for common questions
    reactor_questions = [
        "reactor", "cstr", "batch", "pfr", "conversion", "residence time", "reaction"
    ]
    
    separation_questions = [
        "filter", "filtration", "centrifuge", "flotation", "classifier", "separation"
    ]
    
    size_reduction_questions = [
        "crusher", "mill", "grinding", "size reduction", "trommel", "screen"
    ]
    
    report_questions = [
        "report", "table", "graph", "figure", "calculation", "format"
    ]
    
    # Check question type and generate appropriate response
    question_lower = question.lower()
    
    if any(term in question_lower for term in reactor_questions):
        return """
        **Reactor Systems**:
        
        Chemical reactors are vessels designed to contain chemical reactions. The main types are:
        
        1. **Batch Reactor**: All reactants are added at the start and the reaction proceeds over time.
           - Conversion increases with time.
           - Used for small-scale production and testing.
        
        2. **CSTR (Continuous Stirred Tank Reactor)**: Reactants flow in continuously and products flow out.
           - Well-mixed, uniform composition throughout.
           - Steady-state operation with constant conversion.
        
        3. **PFR (Plug Flow Reactor)**: Tubular reactor with reactants flowing continuously.
           - Concentration varies along the length of the reactor.
           - Higher conversion than CSTR for the same volume.
           
        4. **Semi-Batch Reactor**: Some reactants added initially, others added over time.
           - Allows better temperature control for exothermic reactions.
           
        The key parameter is residence time (τ), which affects conversion. Longer residence time generally leads to higher conversion.
        """, "Built-in knowledge"
        
    elif any(term in question_lower for term in separation_questions):
        return """
        **Solid-Liquid Separation Techniques**:
        
        1. **Filtration**:
           - Filter Press: Batch operation with multiple plates and frames.
           - Rotary Vacuum Filter: Continuous operation with a rotating drum.
           - Driving force is pressure differential (gravity, vacuum, or applied pressure).
        
        2. **Centrifugation**:
           - Uses centrifugal force to separate particles based on density.
           - Basket centrifuges: Solid collects on the walls of a perforated basket.
           - Higher rpm increases separation efficiency but requires more energy.
        
        3. **Flotation**:
           - Separates particles based on surface properties.
           - Air bubbles attach to hydrophobic particles and float them to the surface.
           - Collectors and frothers are added to enhance separation.
        
        4. **Classification**:
           - Separates particles by size or density in a fluid medium.
           - Hydraulic classifiers use upward flow of water.
           - Thickeners use gravity to concentrate slurries.
        """, "Built-in knowledge"
        
    elif any(term in question_lower for term in size_reduction_questions):
        return """
        **Size Reduction Equipment**:
        
        1. **Crushers**:
           - Jaw crushers: Compression between moving and fixed plates.
           - Gyratory crushers: Compression between eccentric rotating cone and fixed cone.
           - Used for coarse and medium crushing.
        
        2. **Ball Mills**:
           - Rotating cylinder with steel balls that crush material by impact and attrition.
           - Critical speed: Speed at which balls centrifuge against the wall.
           - Optimal operation is at 70-80% of critical speed.
        
        3. **Trommel**:
           - Rotary cylindrical screen for particle classification.
           - Inclined to facilitate material flow.
           - Separation efficiency depends on rotation speed, inclination, and feed rate.
        
        Size reduction follows laws relating energy input to particle size change:
        - Kick's Law: Energy proportional to size reduction ratio (coarse crushing)
        - Rittinger's Law: Energy proportional to new surface area created (fine grinding)
        - Bond's Law: Intermediate between Kick's and Rittinger's (most widely used)
        """, "Built-in knowledge"
        
    elif any(term in question_lower for term in report_questions):
        return """
        **Laboratory Report Guidelines**:
        
        A complete chemical engineering lab report should include:
        
        1. **Title Page**: Experiment name, your name, date, course information.
        
        2. **Abstract**: Brief summary of the experiment (objectives, methods, key results).
        
        3. **Introduction**: Background information and theoretical principles.
        
        4. **Aim & Objectives**: Clear statement of purpose and specific goals.
        
        5. **Experimental Procedure**: Equipment, materials, and step-by-step methodology.
        
        6. **Observations & Data**: Raw data in properly formatted tables.
        
        7. **Calculations**: Sample calculations with equations and units clearly shown.
        
        8. **Results**: Processed data, graphs, and tables with proper labels.
        
        9. **Discussion**: Interpretation of results, comparison with theory, error analysis.
        
        10. **Conclusions**: Summary of findings related to objectives.
        
        11. **References**: Properly cited sources.
        
        The report generation feature in this simulator allows you to automatically create reports with your experimental data.
        """, "Built-in knowledge"
    
    else:
        return """
        I'm your Chemical Engineering Assistant! I can help with questions about:
        
        - Reactor systems (batch, CSTR, PFR)
        - Separation techniques (filtration, centrifugation, flotation)
        - Size reduction equipment (crushers, ball mills, trommel)
        - Laboratory report preparation
        
        For more specialized or general chemical engineering questions, please enable the External API option at the top of the page.
        """, "Built-in knowledge"


def generate_response_with_api(question, api_key=None):
    """
    Generates a response based on the user's question, using API for specialized questions.
    
    Args:
        question (str): The user's question
        api_key (str, optional): Hugging Face API token for more general responses
        
    Returns:
        tuple: (response_text, source) - The response text and its source
    """
    # First, check if it's a math calculation
    math_result, is_math = math_calculator(question)
    if is_math:
        return math_result, "Calculator"
    
    # First try to match with built-in knowledge
    reactor_questions = [
        "reactor", "cstr", "batch", "pfr", "conversion", "residence time", "reaction"
    ]
    
    separation_questions = [
        "filter", "filtration", "centrifuge", "flotation", "classifier", "separation"
    ]
    
    size_reduction_questions = [
        "crusher", "mill", "grinding", "size reduction", "trommel", "screen"
    ]
    
    report_questions = [
        "report", "table", "graph", "figure", "calculation", "format"
    ]
    
    # Check question type and generate appropriate response
    question_lower = question.lower()
    
    # Check if the question matches our built-in knowledge categories
    if any(term in question_lower for term in reactor_questions):
        return generate_response_builtin(question)
    elif any(term in question_lower for term in separation_questions):
        return generate_response_builtin(question)
    elif any(term in question_lower for term in size_reduction_questions):
        return generate_response_builtin(question)
    elif any(term in question_lower for term in report_questions):
        return generate_response_builtin(question)
    
    # If no match with built-in categories, try using the API
    if api_key:
        try:
            # Get the selected model from session state
            model = st.session_state.get("selected_model", "google/flan-t5-xxl")
            return get_huggingface_response(question, api_key, model)
        except Exception as e:
            st.error(f"Error connecting to Hugging Face API: {str(e)}")
            return """
            I'm sorry, I encountered an error connecting to the Hugging Face API. Please check your API token or try again later.
            
            In the meantime, I can help with these chemical engineering topics:
            - Reactor systems (batch, CSTR, PFR)
            - Separation techniques (filtration, centrifugation, flotation)
            - Size reduction equipment (crushers, ball mills, trommel)
            - Laboratory report preparation
            """, "Error - API Connection Failed"
    
    else:
        return """
        I don't have enough information to answer that question using my built-in knowledge.
        
        Please check that you have:
        1. Enabled the External API option at the top of the page
        2. Provided a valid Hugging Face API token
        
        Or try asking a question about one of these topics:
        - Reactor systems (batch, CSTR, PFR)
        - Separation techniques (filtration, centrifugation, flotation)
        - Size reduction equipment (crushers, ball mills, trommel)
        - Laboratory report preparation
        """, "Built-in knowledge - Limited Information"


def get_huggingface_response(question, api_key, model="google/flan-t5-xxl"):
    """
    Get a response from Hugging Face API for chemical engineering questions
    
    Args:
        question (str): User's question
        api_key (str): Hugging Face API token
        model (str): Hugging Face model ID to use
        
    Returns:
        tuple: (response_text, source) - The response text and "Hugging Face API" as source
    """
    # Set API URL with the selected model
    API_URL = f"https://api-inference.huggingface.co/models/{model}"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Prepare the prompt based on the model type
    if "t5" in model:
        # For T5 models, we need to add a prefix
        prompt = f"Answer the following chemical engineering question: {question}"
    elif "bart" in model:
        # For BART models, let's use a summarization approach
        prompt = f"Chemical engineering question: {question}\nDetailed answer:"
    elif "roberta" in model or "bert" in model:
        # For BERT/RoBERTa models, we need to format as question-answer
        prompt = {
            "question": question,
            "context": "Chemical engineering is a branch of engineering that uses principles of chemistry, physics, mathematics, biology, and economics to efficiently use, produce, design, transport and transform energy and materials. The work of chemical engineers can range from the utilization of nanotechnology and nanomaterials in the laboratory to large-scale industrial processes that convert chemicals, raw materials, living cells, microorganisms, and energy into useful forms and products."
        }
    else:
        # Default prompt
        prompt = f"""
        As a chemical engineering expert, please answer the following question 
        with accurate and educational information:
        
        {question}
        """
    
    # Prepare the payload based on model type
    if "roberta" in model or "bert" in model and isinstance(prompt, dict):
        payload = prompt
    else:
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_length": 500,
                "temperature": 0.7,
                "top_p": 0.95,
                "do_sample": True
            }
        }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        
        # Handle the response format based on the model type
        if "roberta" in model or "bert" in model:
            if isinstance(result, list) and len(result) > 0:
                answer = result[0].get("answer", "")
            else:
                answer = str(result)
        else:
            # The response format may vary depending on the model
            if isinstance(result, list) and len(result) > 0:
                answer = result[0].get("generated_text", "")
            elif isinstance(result, dict):
                answer = result.get("generated_text", "")
            else:
                answer = str(result)
        
        model_name = model.split("/")[-1].upper()
        return answer, f"Hugging Face API ({model_name})"
    else:
        error_message = f"API Error: {response.status_code} - {response.text}"
        raise Exception(error_message) 