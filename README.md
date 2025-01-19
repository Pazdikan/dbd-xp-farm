## Key Features
- ✨ **Anti-AFK System**: Smart movement patterns to prevent disconnection
- 🛡️ **Anti-Banner Protection**: Handles disconnections and loading screen issues
- 🎮 **Killer-Specific Actions**: Optimized behaviors for bloodpoint farming
- 🌐 **Web Control Panel**: Remote management interface
- 📊 **In-Game Overlay**: Real-time stats and logging display
- 📈 **Very Powerful**: Up to 2500xp per hour (6000xp during double xp event)

## How It Works
The script keeps your killer moving and doing their thing to look like a real player. Each killer has their own actions they'll use - this helps rack up those sweet bloodpoints while keeping everything looking normal. Of course, the script is also farming XP by just being in a game (1 second = 1 xp, cap at 10 minutes)

### Supported Killers
| Killer | Actions |
|--------|----------|
| TRAPPER | Placing and picking up traps |
| BLIGHT | Rushing |
| DOCTOR | Static blast and therapy shock |

## Setup Guide

### Prerequisites
- Python 3.12 (3.13+ not supported)
- NVIDIA CUDA (compatible with all GPUs)

### Installation Steps
1. Clone or download this repository
2. Install Python 3.12
3. Install NVIDIA CUDA from [NVIDIA's website](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64)
    - Select your Windows version
    - Choose "local exe" installer
4. Execute `setup.bat` to install dependencies
5. Launch with `start.bat`

### Configuration
Access the web interface at `http://localhost:5000` to customize script settings.

You can also access the web interface from a different machine, at `http://your-pc-local-ip:5000`

## Interface Screenshots

### Control Panel
<img src=".github/webserver.png" alt="Web Control Panel" width="400px">

### In-Game Display
<img src=".github/overlay.png" alt="In-Game Overlay" width="100%">

## Disclaimer
While AFK farming hasn't led to widespread bans and can benefit other players through gameplay mechanics, use this script at your own risk. The developer assumes no responsibility for any potential account actions.

Note: The script uses isolated virtual environments to prevent Python package conflicts.
