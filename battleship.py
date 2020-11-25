from flask import *
import random

PLAYING = True

# Defining ship class
# Tuple (x, y) for position and state for if it's alive
class Ship():
    def __init__(self, pos, state):
        self.pos = pos
        self.state = state

# Initialize and return the board
# 4x4 grid of "O" chars
def makeBoard():
    board = [["O" for i in range(4)] for k in range(4)]

    for i in range(4):
        board[i] = ["O"] * 4 # Prevents aliasing
    return board

# Display the board to the shell w/ axis numbering
def printBoard(board):
    for k in range(4):
        print(f"\t{k}", end="", flush=True)
    print("\n")

    for i in range(4):
        print(i, end="\t")
        print("\t".join(board[i]))

# Instantiates a living ship with a random position
def randShip():
    return Ship((random.randint(0, 3), random.randint(0, 3)), True)

# Allows the player to place a ship at the start of a game
def placeShip(board, x, y):
    place = (x, y)
    board[place[1]][place[0]] = "P"
    return Ship(place, True)

# If you win, the game ends and you get a fun message
def win():
    global PLAYING
    print("You Win!")
    PLAYING = False

def lose():
    global PLAYING
    print("You Lose!")
    PLAYING = False

# Actual game logic:
# Gets move from player, puts it into a tuple, and checks for a hit or miss
# Also sanitizes the input to make sure the player doesn't give invalid numbers
def procMove(board, enemy):
    target = tuple(map(int, input("x, y coords: ").split(' ')))
    x = target[0]
    y = target[1]

    if x > 3 or x < 0 or y > 3 or y < 0:
        print("Invalid input, please try again\n")
        target = tuple(map(int, input("x, y coords: ").split(' ')))

    if enemy.pos[0] == x and enemy.pos[1] == y:
        board[y][x] = "X"
        print("Hit!")
        win()
    else:
        board[y][x] = "M"
        print("Miss!")

# Computer will guess random coordinates from the board and update board for hit or miss
# Takes as input the board, the player ship, and the computer ship
def compMove(board, player, self):
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    if player.pos[0] == x and player.pos[1] == y:
        check = True
        while check:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if player.pos[0] != x or player.pos[1] != y:
                check = False
    if player.pos[0] == x and player.pos[1] == y:
        board[y][x] = "X"
        flash("Comp Hit! You lose")
    else:
        board[y][x] = "M"
        flash("Comp Miss!")

# Driver code
def main():
    global PLAYING
    board = makeBoard()
    player = placeShip(board)
    enemy = randShip()
    printBoard(board)
    while(PLAYING):
        procMove(board, enemy)
        compMove(board, player, enemy)

if __name__ == "__main__":
    main()
