print("Tic Tac Toe\n")

# startInput = input("Press S to start, ")


playerTurn = 1
playerDidWin = False
print("You are Player 1, which is X.\nGrids are A1-A3, B1-B3, C1-C3")
# inputX = input("Player 1 go, you may type in this format 'top-L', 'mid-L', 'low-L': ")
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def pBoard(board):
    print("\n-=-=-=-=-=-=-=-=-=-=\n")
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def handleInputX():
    playerTurn = 1
    inputX = input("\nPlayer 1 go, you may type in this format 'top-L', 'mid-L', 'low-L': ")
    if playerTurn == 1:
        if inputX == 'top-L':
            theBoard.update({'top-L': 'X'})
        if inputX == 'top-M':
            theBoard.update({"top-M": "X"})

        if inputX == 'mid-R':
            theBoard.update({"top-R": 'X'})
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


def handleInputO():
    playerTurn = 2
    inputX = input("\nPlayer 2 go, you may type in this format 'top-L', 'mid-L', 'low-L': ")
    if playerTurn == 2:

        if inputX == 'top-L':
            theBoard.update({'top-L': 'O'})
        if inputX == 'top-M':
            theBoard.update({"top-M": "O"})

        if inputX == 'top-R':
            theBoard.update({"top-R": "O"})

        if inputX == 'mid-L':
            theBoard.update({"mid-L": "O"})

        if inputX == 'mid-M':
            theBoard.update({"mid-M": "O"})

        if inputX == 'mid-R':
            theBoard.update({"mid-R": "O"})

        if inputX == 'low-L':
            theBoard.update({"low-L": "O"})

        if inputX == 'low-M':
            theBoard.update({"low-M": "O"})

        if inputX == 'low-R':
            theBoard.update({"low-R": "O"})


# printBoard and theBoard code from https://medium.com/@pk1288780/creating-tic-tac-toe-in-python-using-dictionaries
# -70ab8ab49a19

while playerDidWin != True:
    handleInputX()
    pBoard(theBoard)
    playerTurn += 1

    handleInputO()
    pBoard(theBoard)
    playerTurn -= 1

if (
        theBoard['top-L'] == "X" and theBoard['mid-L'] == "X" and theBoard['low-L'] == "X"
        or
        theBoard['top-M'] == "X" and theBoard['mid-M'] == "X" and theBoard['low-M'] == "X"
        or
        theBoard['top-R'] == "X" and theBoard['mid-R'] == "X" and theBoard['low-R'] == "X"
        or
        theBoard['top-L'] == "X" and theBoard['top-M'] == "X" and theBoard['top-R'] == "X"
        or
        theBoard['mid-L'] == "X" and theBoard['mid-M'] == "X" and theBoard['mid-R'] == "X"
        or
        theBoard['low-L'] == "X" and theBoard['low-M'] == "X" and theBoard['low-R'] == "X"
        or
        theBoard['top-R'] == "X" and theBoard['mid-R'] == "X" and theBoard['low-R'] == "X"
        or
        theBoard['top-L'] == "X" and theBoard['mid-M'] == "X" and theBoard['low-R'] == "X"
        or
        theBoard['top-R'] == "X" and theBoard['mid-M'] == "X" and theBoard['low-L'] == "X"

):
    playerDidWin = True

if playerDidWin == True:
    print("Player ", playerTurn, " has won!")

# print("You are Player 2 which is O.\nGrids are A1-A3, B1-B3, C1-C3")
# input("Player 2 go, you may type in this format 'top-L', 'mid-L', 'low-L': ")


# printBoard(theBoard)
