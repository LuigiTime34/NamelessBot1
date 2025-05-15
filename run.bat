@echo off
echo Checking for virtual environment...

:: Check if .venv directory exists
if not exist .venv (
  echo No virtual environment found. Creating one...
  uv venv
  if %ERRORLEVEL% neq 0 (
    echo Error creating virtual environment. Exiting.
    exit /b 1
  )
  echo Virtual environment created successfully.
)

echo Ensuring dependencies for Main are up to date...
:: This command installs/updates/removes packages to match requirements.txt
uv pip sync requirements.txt

:: Check if the sync command was successful before running the bot
if %ERRORLEVEL% neq 0 (
  echo Error syncing dependencies. Exiting.
  exit /b 1
)

:: Activate environment if needed (uv run often handles this)
:: call .venv\Scripts\activate.bat
echo Starting Main...
uv run python main.py