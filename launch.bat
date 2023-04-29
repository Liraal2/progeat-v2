@echo off
REM This is a batch script to safely launch Python script progeat-v2.0.py.

REM Check if Python is installed and in the system path
where python >nul 2>nul
if %errorlevel% neq 0 (
echo Python not found. Please install Python or add it to the system PATH.
pause
exit /b 1
)

REM Check if progeat-v2.0.py exists in the current directory
if not exist progeat-v2.0.py (
echo progeat-v2.0.py not found in the current directory.
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
echo venv virtual environment not found. Running setup script to create and configure the virtual environment...
REM Ensure setup script exists in the current directory
if not exist setup.bat (
echo setup.bat not found in the current directory.
pause
exit /b 1
)
call setup.bat skip_pause
)

REM Activate the venv virtual environment
call venv\Scripts\activate.bat

REM Set the PYTHONIOENCODING to utf-8 to handle Unicode characters
set PYTHONIOENCODING=utf-8

REM Launch the Python script and handle any exceptions
echo Starting progeat-v2.0.py...
python progeat-v2.0.py 2> error.log
if %errorlevel% neq 0 (
echo An error occurred while running progeat-v2.0.py. Please check error.log for more details.
pause
exit /b 1
)

REM If everything runs successfully, inform the user and exit
echo progeat-v2.0.py executed successfully!
pause

REM Deactivate the venv virtual environment
call venv\Scripts\deactivate.bat

exit /b 0