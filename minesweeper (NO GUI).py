import random
import os

SQUARE_TYPE = ["MINE", "CLEAR", "CLEAR", "CLEAR", "CLEAR", "CLEAR", "CLEAR", "CLEAR", "CLEAR"]
POSITIONS = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
game_assignments = [] #stores the game field


def start_game():
    '''Assigns square types to each square'''
    for pos in POSITIONS:
        sqr = random.choice(SQUARE_TYPE)
        SQUARE_TYPE.remove(sqr)
        game_assignments.append((pos, sqr))
    return game_assignments

start_game()

def mine_loc():
    """Returns square with mine"""
    for square in game_assignments:
        if square[1] == "MINE":
            return (square[0])

mine_spot = mine_loc()


while True:
    guess_x = input("Avoid the mine. Select the x-coordinate.")
    guess_y = input("Avoid the mine. Select the y-coordinate.")
    guess = int(guess_x), int(guess_y)

    #Ensure that user makes a valid input
    while guess not in POSITIONS:
        guess_x = input("Avoid the mine. Select the x-coordinate.")
        guess_y = input("Avoid the mine. Select the y-coordinate.")
        guess = int(guess_x), int(guess_y)

    if guess == mine_spot:
        print("You lose")
        os.exit()
    else:
        POSITIONS.remove(guess)
        print(POSITIONS)






