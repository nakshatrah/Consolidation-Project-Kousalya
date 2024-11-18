# Tuple Out Dice Game

## 🎲 Project Overview
The **Tuple Out Dice Game** is a two-player game where players take turns rolling dice to accumulate points. Each player rolls three dice, and the goal is to score points without "tupled out," which occurs when all three dice show the same value. The game has special rules about "fixed dice," where if two of the dice show the same value, they are fixed and cannot be rerolled. Players have the option to reroll the remaining dice to try and achieve a better score.

## 🎲Game Rules
- **Tupled Out**: If all three dice show the same number (e.g., 3, 3, 3), the player "tupled out," and their score for that turn is 0.
- **Fixed Dice**: If two dice show the same number (e.g., 4, 4, 5), those two dice are "fixed" and cannot be rerolled. Only the third die can be rerolled.


## 🎲 Features
- **Dice Rolling**: Randomly rolls three dice for each player.
- **Re-roll Mechanism**: Players can re-roll only the non-fixed dice after their first roll.
- **Tupled Out Rule**: If all three dice are the same, the player scores zero points.
- **Score Calculation**: Adds up the dice rolls for scoring, considering any fixed dice.
- **Player Interaction**: Players input their names and make decisions on whether to reroll their dice.

## 🎲 Program Instructions
1. Start the program by running the main script `tuple_out_main.py` in terminal.
2. Input the players names when prompted.
3. Players take turns rolling the dice and can choose to reroll non-fixed dice.
4. The game continues until one player reaches or exceeds a score of 50.

## 🎲 Output
The game will output the following:
- The player's name and their rolls.
- Whether the player "tupled out" and scored zero points.
- The score for the current round and the total score.
- The winner is declared once a player reaches 50 points.
