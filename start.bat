@echo off
if not exist dbdAfk (
    echo "Calling setup.bat to create dbdAfk virtual environment and install dependencies..."
    call setup.bat
)

echo "Activating dbdAfk virtual environment..."
call dbdAfk\Scripts\activate

echo "Running the application..."
python src/main.py
pause