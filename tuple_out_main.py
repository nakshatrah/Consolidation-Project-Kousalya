import random

# create two players
# ask users for their names
p1 = str(input("Player 1, enter your name: "))
p2 = str(input("Player 2, enter your name: "))

#store randomly rolled dice values in a list
p1_rolls = random.choices(range(1,7), k = 3)
p2_rolls = random.choices(range(1,7), k = 3)

# tell player 1 and 2 their dice values they have rolled.
print(f"{p1} you have rolled: {p1_rolls}")
print(f"{p2} you have rolled: {p2_rolls}")

# create a points variable for each of the ps
p1_score = 0
p2_score = 0

#set target score to end the game
target_score = 20

if p1_score >= target_score:
    print(f"{p1} wins with {p1_score} points! ")
elif p2_score >= target_score:
    print(f"{p2} wins with {p2_score} points! ")

# rule: if all 3 dice rolls are the same, player has "tupled out" --> points = 0
def check_tupled_rolls(rolls):
    # check if all three dice are the same (tuple out), score = 0
    # (rolls.count) counts how many times the first roll (rolls[0]) is present 
    # if present 3 times (same roll for all 3), then print tuple out
    if rolls.count(rolls[0]) == 3:
        print("Tupled out! All three dice are the same. ")
        # set the player's score to 0
        return 0

# rule: if 2 dice rolls are the same, those dice are "fixed", cannot re-roll
def check_for_fixed_dice(rolls):
    # create a list of the dice that are "fixed"
    fixed_dice = []

    for roll in rolls:
        # check if there are two duplicates, and ensure that we don't recheck the same pair of rolls
        if ((rolls.count(roll) == 2) and (roll not in fixed_dice)):
            print(f"Two dice are rolled with a value of {roll}, so they are fixed.")
            # add the rolls to the list as "fixed"
            fixed_dice.append(roll)
    
    return(fixed_dice)

    