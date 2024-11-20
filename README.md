# Tuple Out Dice Game

## 🎲 Project Overview
The **Tuple Out Dice Game** is a two-player game where players take turns rolling dice to accumulate points. Each player rolls three dice, and the goal is to score points without "tupled out," which occurs when all three dice show the same value. The game has special rules about "fixed dice," where if two of the dice show the same value, they are fixed and cannot be rerolled. Players can reroll the remaining dice until they choose to stop or they tuple out to try and achieve a better score.


## 🎲Game Rules
- **Fixed Dice**: If two dice show the same number (e.g., 4, 4, 5), those two dice are "fixed" and cannot be rerolled. Only the third die can be rerolled.
- **Tupled Out**: If all three dice show the same number (e.g., 3, 3, 3), the player "tupled out," and their score for that turn is 0.
- **Stopping**: Players can choose to stop rolling at any time. Their score for the turn is the sum of the three dice at that point.
- **Winning**: The first player to reach or exceed 50 points wins the game.


## 🎲 Features
- **Dice Rolling**: Randomly rolls three dice for each player at the start of their turn.
- **Re-roll Mechanism**: Players can reroll non-fixed dice multiple times or stop to lock in their score.
- **Tupled Out Rule**: If all three dice are the same, the player scores zero points for that turn.
- **Score Calculation**: Adds up the values of the three dice at the end of the player's turn.
- **Stopping Mechanism**: Players can decide when to stop rolling to secure their current score.
- **Player Interaction**: Players input their names and decide whether to reroll or stop during their turn.


## 🎲 Program Instructions
1. Start the program by running the main script `tuple_out_main.py` in terminal.
2. Input the players names when prompted.
3. Each player takes turns rolling the dice, deciding whether to reroll or stop.
4. The game continues until one player reaches or exceeds a score of 50.
