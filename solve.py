from board import *

memo = {}

def findMove(state):
    if state in memo:
        return memo[state]

    board, player = state
    end = checkEnd(board)
    if end != -1:
        return -1, end

    # calculations
    moves = listOfMoveIndices(board)
    # initialization
    bestMove = None
    bestScore = None
    foundMove = False

    for move in moves:
        newBoard = list(board)
        newBoard[move] = player
        newState = (tuple(newBoard), other(player))
        _move, score = findMove(newState)

        if not foundMove:
            if player == CROSS:
                # max
                if score == winScores[player]:
                    memo[state] = (move, winScores[player])
                    bestScore = winScores[player]
                    bestMove = move
                    foundMove = True
                elif bestScore is None or bestScore < score:
                    bestMove = move
                    bestScore = score
            else:
                # min
                if score == winScores[player]:
                    memo[state] = (move, winScores[player])
                    bestScore = winScores[player]
                    bestMove = move
                    foundMove = True
                elif bestScore is None or bestScore > score:
                    bestMove = move
                    bestScore = score

    memo[state] = (bestMove, bestScore)
    return (bestMove, bestScore)


winScores = {NOUG: 0, CROSS: 1, TIE: 0.5}
def computeStates():
    initial = [0] * 9
    p1Start = (tuple(initial), NOUG)
    p2Start = (tuple(initial), CROSS)

    findMove(p1Start)
    findMove(p2Start)

    writeStates()


def writeStates():
    with open("lose_state.txt", "w") as f:
        f.write(repr(memo))

computeStates()
