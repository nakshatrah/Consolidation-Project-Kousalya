import random

# create two players and ask users for their names
p1 = str(input("Player 1, enter your name: "))
p2 = str(input("Player 2, enter your name: "))

# store randomly rolled dice values in lists for each player
p1_rolls = random.choices(range(1, 7), k=3)
p2_rolls = random.choices(range(1, 7), k=3)

# create a points variable for each of the players
p1_score = 0
p2_score = 0
#set target score to end the game
target_score = 20

# tell player 1 and 2 their dice values they have rolled.
print(f"{p1} you have rolled: {p1_rolls}")
print(f"{p2} you have rolled: {p2_rolls}")

# rule: if all 3 dice rolls are the same, player has "tupled out" --> points = 0
def check_tupled_rolls(rolls):
    # check if all three dice are the same (tuple out), score = 0
    # (rolls.count) counts how many times the first roll (rolls[0]) is present 
    # if present 3 times (same roll for all 3), then print tuple out
    if rolls.count(rolls[0]) == 3:
        print("Tupled out! All three dice are the same. ")
        # set the player's score to 0
        return 0
    # if there is no tuple, return None
    return None

# rule: if 2 dice rolls are the same, those dice are "fixed", cannot re-roll
def check_fixed_rolls(rolls):
    # create a list of the dice that are "fixed"
    fixed_dice = []
    for roll in rolls:
        # check if there are two duplicates, and ensure that we don't recheck the same pair of rolls
        if ((rolls.count(roll) == 2) and (roll not in fixed_dice)):
            print(f"Two dice are rolled with a value of {roll}, so they are fixed.")
            # add the rolls to the list as "fixed"
            fixed_dice.append(roll)
    return fixed_dice

# function for calculating score based on rolls and fixed dice
def calculate_score(rolls, fixed_dice):
    # calculate the score based on rolls that aren't in fixed_dice
    score = 0
    for roll in rolls:
        # only add the rolls that aren't fixed to score
        if roll not in fixed_dice:
            score += roll
    return score

# main game loop
while ((p1_score < target_score) and (p2_score < target_score)):
    # roll dice for both players
    p1_rolls = random.choices(range(1, 7), k=3)
    p2_rolls = random.choices(range(1, 7), k=3)

    # announce the rolls
    print(f"\n{p1} rolled: {p1_rolls}")
    print(f"{p2} rolled: {p2_rolls}")

    # check and calculate scores for p1
    if check_tupled_rolls(p1_rolls) == 0:
        p1_round_score = 0 # if tupled out, score = 0
    else:
        p1_fixed_dice = check_fixed_rolls(p1_rolls)
        p1_round_score = calculate_score(p1_rolls, p1_fixed_dice)
    p1_score += p1_round_score
    print(f"{p1}'s score this round: {p1_round_score}, Total score: {p1_score}")

    # check and calculate scores for p2
    if check_tupled_rolls(p2_rolls) == 0:
        p2_round_score = 0 # if tupled out, score = 0
    else:
        p2_fixed_dice = check_fixed_rolls(p2_rolls)
        p2_round_score = calculate_score(p2_rolls, p2_fixed_dice)
    p2_score += p2_round_score
    print(f"{p2}'s score this round: {p2_round_score}, Total score: {p2_score}")

# # print the final scores for the round
# print(f"{p1}'s score for this round: {p1_score}")
# print(f"{p2}'s score for this round: {p2_score}")

# check if player 1 or 2 has reached the target score
    if p1_score >= target_score:
        print(f"\n{p1} wins with {p1_score} points!")
        break
    elif p2_score >= target_score:
        print(f"\n{p2} wins with {p2_score} points!")
        break