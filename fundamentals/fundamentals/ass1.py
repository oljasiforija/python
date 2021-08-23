from random import randint

def roll_dice(number = 1, sides = 20, bonus = 0):
    # number and sides - xdy - 2d6, 3d8, 2d10
    # bonus is added to the result of rolling those x dice

    result = bonus

    for x in range(0, number):
        result += randint(1, sides)

    return result
print(roll_dice())