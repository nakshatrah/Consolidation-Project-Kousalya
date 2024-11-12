import random

# create two players and ask users for their names
p1 = str(input("Player 1, enter your name: "))
p2 = str(input("Player 2, enter your name: "))

# store randomly rolled dice values in lists for each player
# create a function instead of manual player rolls
def roll_dice():
    return random.choices(range(1, 7), k=3)

# re-roll feature with fixed dice logic
def reroll_decision(player_name, rolls, fixed_dice):
    # get the indices of fixed dice
    fixed_indices = [i for i, roll in enumerate(rolls) if roll in fixed_dice]
    
    # if all dice are fixed, no need for re-roll
    if len(fixed_indices) == 3:
        print(f"All dice are fixed for {player_name}, no re-roll needed!")
        return rolls
    
    print(f"\n{player_name}'s current rolls are {rolls}. Fixed dice are {fixed_dice}.")
    keep_dice = input(f"Would you like to re-roll (yes/no)? ").lower()
    
    # If they want to re-roll, ask which dice to keep (not the fixed ones)
    if keep_dice == "yes":
        while True:
            keep = input(f"{player_name}, which dice do you want to keep?\nEnter numbers 1, 2, or 3, separated by commas, or type 'all' to re-roll all: ")
            
            if keep == "all":
                # Only re-roll the dice that are not fixed
                rerolled_dice = [random.choice(range(1, 7)) if i not in fixed_indices else rolls[i] for i in range(3)]
                break
            else:
                try:
                    keep_list = [int(i.strip())-1 for i in keep.split(",")]
                    if all(0 <= i < 3 for i in keep_list):
                        # Ensure that the fixed dice aren't re-rolled
                        for i in fixed_indices:
                            if i not in keep_list:
                                keep_list.append(i)
                        rerolled_dice = []
                        for i in range(3):
                            if i not in keep_list:
                                rerolled_dice.append(random.choice(range(1, 7)))
                            else:
                                rerolled_dice.append(rolls[i])
                        break
                    else:
                        print("Invalid input. Please enter numbers 1, 2, or 3.")
                except ValueError:
                    print("Invalid input. Please enter numbers 1, 2, or 3, separated by commas or 'all'.")
        
        # Show the rerolled dice
        print(f"{player_name}'s new rolls after re-rolling: {rerolled_dice}")
        return rerolled_dice
    
    # if the player doesn't want to re-roll, return the same rolls
    return rolls

# create a points variable for each of the players
p1_score = 0
p2_score = 0
#set target score to end the game
target_score = 40

# rule: if all 3 dice rolls are the same, player has "tupled out" --> points = 0
def check_tupled_rolls(rolls, player_name):
    # check if all three dice are the same (tuple out), score = 0
    if rolls.count(rolls[0]) == 3:
        print(f"{player_name}: Tupled out! All three dice are the same.")
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
    # Ensure that the fixed dice are also added to the score
    for roll in rolls:
        score += roll  # Add all dice rolls to score, including fixed ones
    return score

# main game loop
while p1_score < target_score and p2_score < target_score:
    # roll dice for both players
    p1_rolls = roll_dice()
    p2_rolls = roll_dice()

    # announce the rolls
    print(f"\n{p1} rolled: {p1_rolls}")
    print(f"{p2} rolled: {p2_rolls}")

    # check and calculate scores for p1
    p1_round_score = check_tupled_rolls(p1_rolls, p1)
    if p1_round_score is None:
        p1_fixed_dice = check_fixed_rolls(p1_rolls)
        p1_rolls = reroll_decision(p1, p1_rolls, p1_fixed_dice)
        p1_round_score = calculate_score(p1_rolls, p1_fixed_dice)
    
    p1_score += p1_round_score
    print(f"{p1}'s score this round: {p1_round_score}, Total score: {p1_score}")

    # check and calculate scores for p2
    p2_round_score = check_tupled_rolls(p2_rolls, p2)
    if p2_round_score is None:
        p2_fixed_dice = check_fixed_rolls(p2_rolls)
        p2_rolls = reroll_decision(p2, p2_rolls, p2_fixed_dice)
        p2_round_score = calculate_score(p2_rolls, p2_fixed_dice)
    
    p2_score += p2_round_score
    print(f"{p2}'s score this round: {p2_round_score}, Total score: {p2_score}")

    # check if player 1 or 2 has reached the target score
    if p1_score >= target_score:
        print(f"\n{p1} wins with {p1_score} points!")
        break
    elif p2_score >= target_score:
        print(f"\n{p2} wins with {p2_score} points!")
        break