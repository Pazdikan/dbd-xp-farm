> [!WARNING]  
> This script is designed for 1920x1080 display. If you are using a higher resolution display please set it to 1920x1080 in windows' display settings.

# An AFK Script for Dead by Daylight

## Setup
1. Download and unpack this repository
2. Install python 3.11+
3. Install python requirements (setup.bat, first time only):
```
pip install -r requirements.txt
```
4. Run the script (start.bat):
```
python run.py
```

## Features
- [X] Queueing
- [X] Attacking
- [X] Random Movement
- [X] Statistics
- [X] Different behaviour for different killers (for bloodpoints)
- [ ] Settings (ui + saving)


# Behaviors
All killers walk forward-backward and attack. Some time ago BHVR added an anti-afk system which make you "DC" after the game (so you won't get xp and bloodpoints). You can even hit survivors, but if you didn't move an inch you will get kicked.

| Killer | Actions |
|-|-|
| <img src=".github/TheTrapper.webp" alt="drawing" width="150"/> | - Placing and picking up traps<br>