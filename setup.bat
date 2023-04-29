@echo off
REM This is a batch script to set up a Python virtual environment venv
REM and install all libraries from the requirements.txt file

REM Check if Python is installed and in the system path
where python >nul 2>nul
if %errorlevel% neq 0 (
echo Python not found. Please install Python or add it to the system PATH.
pause
exit /b 1
)

REM Check if requirements.txt exists in the current directory
if not exist requirements.txt (
echo requirements.txt not found in the current directory.
pause
exit /b 1
)

REM Check if Python is the required version (e.g., 3.6 or newer)
for /f "tokens=2 delims=. " %%i in ('python --version 2^>^&1') do set python_major=%%i
if %python_major% LSS 3 (
echo Python 3.6 or newer is required. Please update your Python installation.
pause
exit /b 1
)

REM Check if venv venv exists
if not exist venv (
echo venv virtual environment not found. Creating a new virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
echo An error occurred while creating the virtual environment. Please check your Python installation.
pause
exit /b 1
)
)

REM Activate the venv virtual environment
call venv\Scripts\activate.bat

REM Install all libraries from the requirements.txt file
echo Installing libraries from requirements.txt...
pip install -r requirements.txt
if %errorlevel% neq 0 (
echo An error occurred while installing the libraries. Please check your requirements.txt file.
pause
exit /b 1
)

REM Inform the user of successful installation and exit
echo All libraries installed successfully!

REM Deactivate the venv virtual environment
call venv\Scripts\deactivate.bat

REM Check if the script was called from the launch script
if "%1" == "skip_pause" (
    exit /b 0
)

REM Pause if the script was not called from the launch script
pause
exit /b 0