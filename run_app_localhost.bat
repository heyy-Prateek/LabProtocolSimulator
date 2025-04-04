@echo off
echo Starting Chemical Engineering Lab Simulator at http://127.0.0.1:5000
echo Press Ctrl+C to stop the server

call venv\Scripts\activate.bat
streamlit run app.py

pause 