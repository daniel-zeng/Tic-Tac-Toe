symbols = {0: "-", 1: "O", 2: "X"}
NOUG = 1
CROSS = 2
TIE = 3
width = 3
endGame = {NOUG: 1, CROSS: 0, TIE: 0.5}

class Board:
    def __init__(self, case):
        self.board = [0] * 9
        self.case = case
        global endGame
        if case == 1:
            self.memo = self.loadMemo("win_state.txt")
            endGame = {NOUG: 1, CROSS: 0, TIE: 0.5}
        elif case == 2:
            self.memo = self.loadMemo("lose_state.txt")
            endGame = {NOUG: 0, CROSS: 1, TIE: 0.5}

    def loadMemo(self, fname):
        try:
            with open(fname, "r") as f:
                return eval(f.readline())
        except FileNotFoundError:
            print("Please run solve.py to generated computed states")
            exit(2)

    def startGame(self):
        while 1:
            if self.gameLoop():
               break

    def gameLoop(self):
        # do p1 move
        ro, co = getInput(self.board)
        print()
        # co = input("Player 1 col: ")
        placePiece(self.board, ro, co, NOUG)

        print("Player 1 (O) goes")
        printBoard(self.board)
        print()
        print()

        if checkWinner(checkEnd(self.board)):
            return True

        # do p2 move
        state = (tuple(self.board), CROSS)
        move, _score = self.memo[state]
        assert move > -1 or move < 9
        ro2, co2 = intMoveToRC(move)
        # print(state, "-", move)
        placePiece(self.board, ro2, co2, CROSS)

        print("Player 2 (X) goes")
        printBoard(self.board)
        print()
        print()

        if checkWinner(checkEnd(self.board)):
            return True

        return False

def getInput(data):
    print("Player 1 (O) move:")
    bounds = range(3)
    while 1:
        ro = processInput("Row: ", bounds, int)
        co = processInput("Column: ", bounds, int)
        pos = ro * width + co
        if data[pos] == 0:
            return ro, co
        else:
            print("That position already has a piece, try again")

def processInput(stri, bounds, type):
    # print(bounds)
    while 1:
        res = input(stri)
        val = None
        try:
            val = type(res) - 1
        except ValueError:
            print("Input not an integer, try again")
            continue

        if val in bounds:
            return val
        else:
            print("Value out of bounds")



def checkWinner(val):
    # print(endGame[3])

    if val == -1:
        return False
    if val == endGame[NOUG]:
        print("Player 1 wins")
    elif val == endGame[CROSS]:
        print("Player 2 wins")
    elif val == endGame[TIE]:
        print("Game is tied")
    return True



def printBoard(arr):
    count = 0
    start = False
    for i in range(len(arr)):
        if count % width == 0 and start:
            print()
        print(symbols[arr[i]], end=" ")
        count += 1
        start = True


def placePiece(data, row, co, piece):
    pos = row * width + co
    assert piece == CROSS or piece == NOUG
    assert row >= 0 or row < width and co >= 0 or co < width
    assert data[pos] == 0
    data[pos] = piece


def threeInRow(data, player):
    first = data[0] == player and data[1] == player and data[2] == player
    second = data[3] == player and data[4] == player and data[5] == player
    third = data[6] == player and data[7] == player and data[8] == player
    return first or second or third


def threeInCol(data, player):
    first = data[0] == player and data[3] == player and data[6] == player
    second = data[1] == player and data[4] == player and data[7] == player
    third = data[2] == player and data[5] == player and data[8] == player
    return first or second or third


def threeInDiag(data, player):
    first = data[0] == player and data[4] == player and data[8] == player
    second = data[2] == player and data[4] == player and data[6] == player
    return first or second


# hardcoded for width=3
def checkWin(data, player):
    return threeInCol(data, player) or threeInDiag(data, player) or threeInRow(data, player)


def checkEnd(data):
    fixedEnd = {NOUG: 1, CROSS: 0, TIE: 0.5}

    # p1 win
    if checkWin(data, NOUG):
        return fixedEnd[NOUG]
    # p2 win
    if checkWin(data, CROSS):
        return fixedEnd[CROSS]
    # tie case
    if len([e for e in data if e != 0]) == 9:
        return fixedEnd[TIE]
    # no win
    return -1


def listOfMoveIndices(data):
    return [i for i in range(len(data)) if data[i] == 0]


def other(player):
    assert player == NOUG or player == CROSS
    return TIE - player


def intMoveToRC(move):
    return (move // 3, move % 3)
