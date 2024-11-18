import random

# create two players and ask users for their names
p1 = str(input("player 1, enter your name: "))
p2 = str(input("player 2, enter your name: "))

# store randomly rolled dice values in lists for each player
# create a function instead of manual player rolls
def roll_dice():
    return random.choices(range(1, 7), k=3)

# re-roll feature with fixed dice logic
def reroll_decision(player_name, rolls, fixed_dice):
    # get the indices of fixed dice
    fixed_indices = [i for i, roll in enumerate(rolls) if roll in fixed_dice]
    
    # tell the player the current rolls and fixed dice
    print(f"\n{player_name}'s current rolls are {rolls}. fixed dice are {fixed_dice}.")

    # ask the player if they want to reroll
    reroll_choice = input(f"{player_name}, would you like to reroll your dice? enter 'yes' to reroll or 'no' to keep your current rolls: ").lower()
    
    # handle invalid input
    while reroll_choice not in ['yes', 'no']:
        reroll_choice = input("invalid choice. please enter 'yes' or 'no': ").lower()

    if reroll_choice == "yes":
        # reroll only the non-fixed dice
        rerolled_dice = [
            random.choice(range(1, 7)) if i not in fixed_indices else rolls[i]
            for i in range(3)
        ]
        
        print(f"\n{player_name}'s new rolls after reroll: {rerolled_dice}")
        return rerolled_dice

    # if the player doesn't want to re-roll, return the same rolls
    print(f"\n{player_name} chose not to reroll. rolls remain: {rolls}")
    return rolls

# create a points variable for each of the players
p1_score = 0
p2_score = 0
# set target score to end the game
target_score = 50

# rule: if all 3 dice rolls are the same, player has "tupled out" --> points = 0
def check_tupled_rolls(rolls, player_name):
    # check if all three dice are the same (tuple out), score = 0
    if rolls.count(rolls[0]) == 3:
        print(f"{player_name}: tupled out! all three dice are the same.")
        return 0
    return None

# rule: if 2 dice rolls are the same, those dice are "fixed", cannot re-roll
def check_fixed_rolls(rolls):
    fixed_dice = []
    for roll in rolls:
        if rolls.count(roll) == 2 and roll not in fixed_dice:
            fixed_dice.append(roll)
    return fixed_dice

# function for calculating score based on rolls and fixed dice
def calculate_score(rolls, fixed_dice):
    score = 0
    # ensure that the fixed dice are also added to the score
    for roll in rolls:
        # add all dice rolls to score, including fixed ones
        score += roll
    return score

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
            print("\nit's a tie!")
        break
    elif p1_score >= target_score:
        print(f"\n{p1} wins with {p1_score} points!")
        break
    elif p2_score >= target_score:
        print(f"\n{p2} wins with {p2_score} points!")
        break