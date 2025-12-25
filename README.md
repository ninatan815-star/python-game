# Platform Game - Pygame Zero Project

## Quick Start

1. Extract the `platformer_game.zip` file
2. Open Mu Editor
3. Click "Mode" and select "Pygame Zero"
4. Open `main.py` from the extracted folder
5. Click "Play" to run the game!

## Controls

- **Arrow Keys (Left/Right)**: Move the player
- **Space or Up Arrow**: Jump
- **Mouse**: Click menu buttons

## Game Objective

- Navigate from left to right
- Avoid the red enemies (they patrol back and forth)
- Reach the right side of the screen (x > 700) to win!
- If you touch an enemy, you lose

## Menu Options

- **Start Game**: Begin playing
- **Music Toggle**: Turn background music on/off
- **Exit**: Close the game

## Files Included

```
platformer_game/
├── main.py                    # Main game code (run this!)
├── images/
│   ├── hero_idle1.png        # Hero standing frame 1
│   ├── hero_idle2.png        # Hero standing frame 2
│   ├── hero_walk1.png        # Hero walking frame 1
│   ├── hero_walk2.png        # Hero walking frame 2
│   ├── enemy_idle1.png       # Enemy frame 1
│   ├── enemy_idle2.png       # Enemy frame 2
│   ├── enemy_walk1.png       # Enemy walking frame 1
│   └── enemy_walk2.png       # Enemy walking frame 2
├── sounds/
│   └── jump.wav              # Jump sound effect
└── music/
    └── background.wav        # Background music (loops)
```

## Troubleshooting

**Game doesn't start:**
- Make sure you're in "Pygame Zero" mode in Mu Editor
- Ensure all files are in the correct folders

**No sound:**
- Check your computer's volume
- Sound files must be in the `sounds/` and `music/` folders

**Can't see sprites:**
- Make sure the `images/` folder is in the same directory as `main.py`

## Customization Ideas

1. **Change colors**: Edit the RGB values in the `draw()` function
2. **Add more enemies**: Add entries to the `baddies` list
3. **Adjust difficulty**: Change enemy speed or patrol ranges
4. **Modify physics**: Adjust GRAVITY, jump velocity, or movement speed

## Code Structure

- **AnimatedSprite**: Base class for all animated characters
- **Hero**: Player character with jumping and movement
- **Enemy**: AI-controlled enemies with patrol behavior
- **Game States**: menu, playing, win, lose

Enjoy the game!
