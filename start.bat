@echo off
echo Chemical Engineering Laboratory Simulator
echo ========================================
echo.
echo Select an option:
echo 1. Run Full Application
echo 2. Run API Server Only
echo 3. Run Streamlit UI Only
echo 4. Build React Frontend
echo 5. Exit
echo.

set /p choice=Enter option (1-5): 

if "%choice%"=="1" goto run_full
if "%choice%"=="2" goto run_api
if "%choice%"=="3" goto run_ui
if "%choice%"=="4" goto build_react
if "%choice%"=="5" goto exit_script

echo Invalid option. Please try again.
echo Press Enter to continue...
pause
cls
goto :eof

:run_full
echo Starting full application...
C:\Users\saxen\AppData\Local\Programs\Python\Python313\python.exe run.py run
echo.
echo Application has stopped. Press Enter to exit.
pause
goto exit_script

:run_api
echo Starting API server only...
C:\Users\saxen\AppData\Local\Programs\Python\Python313\python.exe run.py run --api-only
echo.
echo API server has stopped. Press Enter to exit.
pause
goto exit_script

:run_ui
echo Starting Streamlit UI only...
C:\Users\saxen\AppData\Local\Programs\Python\Python313\python.exe run.py run --streamlit-only
echo.
echo Streamlit UI has stopped. Press Enter to exit.
pause
goto exit_script

:build_react
echo Building React frontend...
C:\Users\saxen\AppData\Local\Programs\Python\Python313\python.exe run.py build --react
echo.
echo Build process complete. Press Enter to exit.
pause
goto exit_script

:exit_script
echo Exiting Chemical Engineering Laboratory Simulator
exit 