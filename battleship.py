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
    
    for i in range(4):       #
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

def placeShip(board):
    place = tuple(map(int, input("x, y coords: ").split(' ')))
    if place[0] > 3 or place[0] < 0 or place[1] > 3 or place[1] < 0:
        print("Invalid coords")
        place = tuple(map(int, input("x, y coords: ").split(' ')))
    else:
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
    PlAYING = False

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
        printBoard(board)
        win()
    else:
        board[y][x] = "M"
        print("Miss!")
        printBoard(board)

def compMove(board, player):
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    if player.pos[0] == x and player.pos[1] == y:
        board[y][x] = "X"
        print("Hit!")
        printBoard(board)
        lose()
    else:
        board[y][x] = "M"
        print("Comp Miss!")
        printBoard(board)
        
# Driver code
def main():
    global PLAYING
    board = makeBoard()
    player = placeShip(board)
    enemy = randShip()
    printBoard(board)
    while(PLAYING):
        procMove(board, enemy)
        compMove(board, player)

if __name__ == "__main__":
    main()