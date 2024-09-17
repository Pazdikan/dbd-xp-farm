# AFK Script for Dead by Daylight

This script is designed to automatically farm XP and a few bloodpoints while avoiding detection:

- **Anti-AFK Proof**: Ensures consistent actions to prevent AFK kicks.
- **Banner-Proof**: Handles cases where survivors disconnect during loading screens.
- **Killer Behaviors**: Implements various killer strategies to maximize bloodpoints gain.
- **XP Gain**: Achieves up to 4000 XP per hour (excluding queue times).
- **Configurable Settings**: Includes settings for customization (more to come).
- **Testing Results**: Tested for 5 hours, yielding ~11,000 XP (queue times took half of that).




## Statistics

(still gathering)

|                         | Per game | Per hour (in-game) |
|-------------------------|----------|--------------------|
| XP (ex. 1st game bonus) | 505 avg  | 3536 avg           |
| Bloodpoints as OTHER    |          |                    |
| Bloodpoints as TRAPPER  | 2321 avg | 16247 avg          |


## Behaviors

All killers follow a basic movement pattern by moving back and forth. This helps bypass the anti-AFK system introduced by BHVR, which disconnects you from the game if no movement is detected. You can still interact with survivors (e.g., hit them), but without any movement, after the game ends you'll be treated like you disconnected (no xp, and matchmaking ban).


| Killer  | Actions                        |
|---------|--------------------------------|
| TRAPPER | - Placing and picking up traps |


## Setup

> [!WARNING]  
> This script is designed for 1920x1080 display. If you are using a higher resolution display please set it to 1920x1080 in windows' display settings.

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


## Settings

You can configure the script's behavior in the `src/config.py` file.

| Variable    | Description                                              | Values         |
|-------------|----------------------------------------------------------|----------------|
| killer      | Select the killer you're using (with custom behavior)    | OTHER, TRAPPER |
| xp_limit    | Script will exit after gaining this much XP              | 0 to disable   |
| games_limit | Script will exit after playing this many games           | 0 to disable   |


## Bans

There's no widespread evidence of players getting banned for AFK farming. Survivors often benefit from it as well (through healing, totems, etc.). 

However, **I am not responsible for any bans** that may occur.
