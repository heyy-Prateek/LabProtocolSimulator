"""
Main entry point for the Chemical Engineering Laboratory Simulator.
"""

import os
import sys
import threading
import argparse
import subprocess

def run_api_server():
    """Run the FastAPI server using uvicorn"""
    import uvicorn
    from chemengsim.api import app
    uvicorn.run(app, host="localhost", port=8000)

def run_streamlit():
    """Run the Streamlit app"""
    streamlit_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.py")
    # Change port from 5000 to 8501 (Streamlit's default port)
    subprocess.run([sys.executable, "-m", "streamlit", "run", streamlit_path, "--server.address=localhost", "--server.port=8501"])

def main():
    """Main entry point for the application"""
    parser = argparse.ArgumentParser(description="Chemical Engineering Laboratory Simulator")
    parser.add_argument("--api-only", action="store_true", help="Run only the API server")
    parser.add_argument("--streamlit-only", action="store_true", help="Run only the Streamlit app")
    args = parser.parse_args()

    if args.api_only:
        run_api_server()
    elif args.streamlit_only:
        run_streamlit()
    else:
        # Run both API server and Streamlit app
        api_thread = threading.Thread(target=run_api_server)
        api_thread.daemon = True
        api_thread.start()
        run_streamlit()

if __name__ == "__main__":
    main()