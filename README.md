# The Last Job - Detective Game

**The Last Job** is a text-based detective game where you play as Sir Thomas Romanov, a skilled detective tasked with solving a mysterious murder. Your survival depends on the decisions you make, your ability to investigate different locations, and ultimately discovering the truth behind the crime.

## MEMBERS
- Kevin Pérez Román



## Table of Contents
- [Introduction](#introduction)
- [Game Mechanics](#game-mechanics)
- [Files](#files)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [License](#license)

## Introduction

In **The Last Job**, you will investigate various areas, interact with different objects, and try to uncover the truth about the murder of Mrs. Natally Stradel. You can explore, use tools, check your inventory, and make decisions that will determine the outcome of the investigation. In the end, you must cast your vote and accuse who you believe is responsible.

## Game Mechanics

- **Exploration**: Investigate various locations to gather clues.
- **Inventory**: Manage the items you collect during the game.
- **Decision Making**: The game will present you with multiple options. Choose wisely, as your decisions affect the outcome.
- **Vote**: After gathering enough evidence, you must decide who committed the crime.

## Files

### `main.py`
This is the core of the game, handling the game loop, player interactions, and the voting system. It controls the flow of the story and provides access to various game features like investigating areas, checking inventory, and moving to new locations.

### `utilities.py`
This file contains utility functions like `show_dialog`, which displays game dialogue with accompanying sound effects, and `clear_screen`, which refreshes the screen.

### `mapa.py`
This file defines the `Map` class and handles map creation and player movement between locations. It also includes the `investigate_area` function, which allows the player to investigate the current area for clues.

### `player.py`
This file contains the `Player` class, which manages the player’s inventory, anxiety levels, and tools. The player can smoke cigarettes to reduce anxiety, reload their gun, or change flashlight batteries based on available resources.

#### Map Overview
- **The Office**
- **The Lounge**
- **The Kitchen**
- **The Master Bedroom**

Each location has interactive objects and clues that the player can investigate.

### Audio
The game uses OpenAL for audio playback. Each action or event can trigger sound effects, adding an immersive experience to the narrative.

## Installation

1. Clone or download the repository.
2. Make sure you have Python 3.6 or higher installed.
3. Install the required libraries:

   ```bash
   pip install pyopenal
   ```

4. Ensure the audio files (e.g., `Teclado.wav`, `Impact.wav`, `Office.wav`) are located in the `Audios` folder.
5. Run the game:

   ```bash
   python main.py
   ```

## How to Play

1. Run `main.py` to start the game.
2. Follow the instructions to navigate through the game's menu.
3. Investigate locations, manage your inventory, and gather clues.
4. Once you've gathered enough information, cast your final vote to solve the mystery.

### Controls

- Use the numeric keys (0-5) to make selections during gameplay.
- Option `0` allows you to surrender and exit the game.

## License

This game is for educational purposes. 

