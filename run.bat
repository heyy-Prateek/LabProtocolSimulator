@echo off
REM Chemical Engineering Laboratory Simulator
REM Windows Batch File for running the application

echo Chemical Engineering Laboratory Simulator
echo ========================================
echo.

IF "%1"=="" (
    echo Available commands:
    echo run         - Run the full application
    echo run-api     - Run only the API server
    echo run-ui      - Run only the Streamlit UI
    echo build-react - Build the React frontend
    echo.
    echo Example: run.bat run
    echo.
    echo Press any key to exit...
    pause > nul
    exit /b 1
)

echo Command selected: %1
echo.

IF "%1"=="run" (
    echo Starting the full application...
    echo.
    python run.py run
    IF %errorlevel% NEQ 0 (
        echo.
        echo Error: Application failed to start. Error code: %errorlevel%
        echo.
        echo Press any key to exit...
        pause > nul
    )
    exit /b %errorlevel%
)

IF "%1"=="run-api" (
    echo Starting API server only...
    echo.
    python run.py run --api-only
    IF %errorlevel% NEQ 0 (
        echo.
        echo Error: API server failed to start. Error code: %errorlevel%
        echo.
        echo Press any key to exit...
        pause > nul
    )
    exit /b %errorlevel%
)

IF "%1"=="run-ui" (
    echo Starting Streamlit UI only...
    echo.
    python run.py run --streamlit-only
    IF %errorlevel% NEQ 0 (
        echo.
        echo Error: Streamlit UI failed to start. Error code: %errorlevel%
        echo.
        echo Press any key to exit...
        pause > nul
    )
    exit /b %errorlevel%
)

IF "%1"=="build-react" (
    echo Building React frontend...
    echo.
    python run.py build --react
    IF %errorlevel% NEQ 0 (
        echo.
        echo Error: React build failed. Error code: %errorlevel%
        echo.
        echo Press any key to exit...
        pause > nul
    ) ELSE (
        echo.
        echo React build completed successfully.
        echo.
        echo Press any key to exit...
        pause > nul
    )
    exit /b %errorlevel%
)

echo Unknown command: %1
echo Run without arguments to see available commands
echo.
echo Press any key to exit...
pause > nul
exit /b 1 