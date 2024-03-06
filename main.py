print("Tic Tac Toe\n")
# startInput = input("Press S to start, ")

print("You are Player 1, which is X.\nGrids are A1-A3, B1-B3, C1-C3")
inputX = input("Player 1 go, you may type in this format 'top-L', 'mid-L', 'low-L': ")
theBoard = {'top-L': '', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def handleInput():
    if (inputX == 'top-L'):
        theBoard.update({'top-L': 'X'})

    if inputX == 'top-R':
        theBoard.update({"top-R": "X"})
    if inputX == 'mid-L':
        theBoard.update({"mid-L": "X"})
    if inputX == 'mid-M':
        theBoard.update({"mid-M": "X"})
    if inputX == 'mid-R':
        theBoard.update({"mid-R": "X"})
    if inputX == 'low-L':
        theBoard.update({"low-L": "X"})
    if inputX == 'low-M':
        theBoard.update({"low-M": "X"})
    if inputX == 'low-R':
        theBoard.update({"low-R": "X"})


# printBoard and theBoard code from https://medium.com/@pk1288780/creating-tic-tac-toe-in-python-using-dictionaries
# -70ab8ab49a19


if inputX == 'top-L':
    theBoard.update({'top-L': 'X'})
    printBoard(theBoard)

# print("You are Player 2 which is O.\nGrids are A1-A3, B1-B3, C1-C3")
# input("Player 2 go, you may type in this format 'top-L', 'mid-L', 'low-L': ")


# printBoard(theBoard)
