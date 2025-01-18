@echo off
if not exist dbdAfk (
    echo "Creating dbdAfk virtual environment for python..."
    python -m venv dbdAfk
)

echo "Checking for NVIDIA CUDA installation..."
where nvcc > nul 2>&1
if %errorlevel% neq 0 (
    echo "WARNING: NVIDIA CUDA not found! Please install CUDA Toolkit (this is for detecting text from game (like buttons))."
    echo "You can download it from: https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64"
    echo ""
    echo "If you did install CUDA, restart your computer and run this script again."
    echo "If it still doesn't work after restart, try google lol and do not open an issue please."
    pause
    exit
)

echo "Activating dbdAfk virtual environment..."
call dbdAfk\Scripts\activate

echo "Installing requirements... This will take a moment depending on your internet speed."

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
pip install -r requirements.txt

echo "Setup complete. Run 'start.bat' to start the bot."
pause