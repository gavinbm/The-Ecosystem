import random

PLAYING = True

class Ship():
    def __init__(self, pos, state):
        self.pos = pos
        self.state = state

def makeBoard():
    board = [["O" for i in range(4)] for k in range(4)]
    
    for i in range(4):
        board[i] = ["O"] * 4
    return board

def printBoard(board):
    for k in range(4):
        num = k
        print(f"\t{num}", end="", flush=True)
    print("\n")
    
    for i in range(4):
        print(i, end="\t")
        print("\t".join(board[i]))

def setShip():
    return Ship((random.randint(0, 3), random.randint(0, 3)), True)
    
def win():
    global PLAYING
    print("You Win!")
    PLAYING = False

def procMove(board, ship2):
    target = tuple(map(int, input("x, y coords: ").split(' ')))
    x = target[0]
    y = target[1]
    
    if x > 3 or x < 0 or y > 3 or y < 0:
        print("Invalid input, please try again\n")
        target = tuple(map(int, input("x, y coords: ").split(' ')))
        
    if ship2.pos[0] == x and ship2.pos[1] == y:
        board[x][y] = "X"
        print("Hit!")
        printBoard(board)
        win()
    else:
        board[x][y] = "M"
        print("Miss!")
        printBoard(board)
        
def main():
    global PLAYING
    board = makeBoard()
    player = setShip()
    enemy = setShip()
    printBoard(board)
    while(PLAYING):
        procMove(board, enemy)

main()