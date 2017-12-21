from board import *
from solve import *

def main():
    prompt()

    val = processInput()
    print()
    b = Board(val)
    b.startGame()

def prompt():
    print("Which game do you want to play?")
    print("1) Normal Tic Tac Toe")
    print("2) Reverse Tic Tac Toe")
    print("/h for help")
    print("/q to quit")

def processInput():
    while 1:
        inpt = input("> ")
        if inpt == "/h":
            print("Normal Tic Tac Toe: Win the game by making three in a row.")
            print("Reverse Tic Tac Toe: Win the game by making the other player make three in a row.")
        elif inpt == "/q":
            exit()
        elif inpt == "1":
            print("You are playing Normal Tic Tac Toe")
            return 1
        elif inpt == "2":
            print("You are playing Reverse Tic Tac Toe")
            return 2
        else:
            print("Input not understood, try again")


if __name__ == '__main__':
    main()