import random

# import the helper functions
from tuple_out_helper_functions import (
    roll_dice,
    reroll_decision,
    check_tupled_rolls,
    check_fixed_rolls,
    calculate_score,
)

# handle a player's turn
def player_turn(player_name, rolls, score):
    print(f"\n{player_name} is taking their turn...")
    print(f"starting rolls: {rolls}")

    # check if tupled out
    round_score = check_tupled_rolls(rolls, player_name)
    if round_score is None:
        # check fixed dice and handle reroll
        fixed_dice = check_fixed_rolls(rolls)
        print(f"fixed dice based on initial roll: {fixed_dice}")
        rolls = reroll_decision(player_name, rolls, fixed_dice)
        
        # recheck for tupled out after reroll
        round_score = check_tupled_rolls(rolls, player_name)
        
        # if still not tupled out
        if round_score is None:
            round_score = calculate_score(rolls, fixed_dice)
    
    score += round_score
    print(f"{player_name}'s score this round: {round_score}, total score: {score}")
    return score

# create two players and ask users for their names
p1 = str(input("Player 1, enter your name: "))
p2 = str(input("Player 2, enter your name: "))

# create a points variable for each of the players
p1_score = 0
p2_score = 0
# set target score to end the game
target_score = 50

# main game loop
while p1_score < target_score and p2_score < target_score:
    # player 1's turn
    p1_score = player_turn(p1, roll_dice(), p1_score)

    # player 2's turn
    p2_score = player_turn(p2, roll_dice(), p2_score)

    # check if player 1 or 2 has reached the target score
    if p1_score >= target_score and p2_score >= target_score:
        # tie-breaking logic if both players reach the target in the same round
        if p1_score > p2_score:
            print(f"\n{p1} wins with {p1_score} points!")
        elif p2_score > p1_score:
            print(f"\n{p2} wins with {p2_score} points!")
        else:
            print("\nIt's a tie!")
        break
    elif p1_score >= target_score:
        print(f"\n{p1} wins with {p1_score} points!")
        break
    elif p2_score >= target_score:
        print(f"\n{p2} wins with {p2_score} points!")
        break