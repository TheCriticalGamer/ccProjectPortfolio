print("Tic Tac Toe\n")

# startInput = input("Press S to start, ")
i = 5

playerTurn = 1
playerDidWin = False
print("You are Player 1, which is X.\nGrids are A1-A3, B1-B3, C1-C3")
# inputX = input("Player 1 go, you may type in this format 'top-L', 'mid-L', 'low-L': ")
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print("\n-=-=-=-=-=-=-=-=-=-=\n")
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def handleInputX():
    inputX = input("\nPlayer 1 go, you may type in this format 'top-L', 'mid-L', 'low-L': ")

    if playerTurn == 1:
        if inputX == 'top-L':
            theBoard.update({'top-L': 'X'})

        if inputX == 'top-M':
            theBoard.update({"top-M": "X"})
        printBoard(theBoard)
        if inputX == 'mid-R':
            theBoard.update({"top-R": 'X'})
        if inputX == 'top-R':
            theBoard.update({"top-R": "X"})
            printBoard(theBoard)
        if inputX == 'mid-L':
            theBoard.update({"mid-L": "X"})
            printBoard(theBoard)
        if inputX == 'mid-M':
            theBoard.update({"mid-M": "X"})
            printBoard(theBoard)
        if inputX == 'mid-R':
            theBoard.update({"mid-R": "X"})
            printBoard(theBoard)
        if inputX == 'low-L':
            theBoard.update({"low-L": "X"})
            printBoard(theBoard)
        if inputX == 'low-M':
            theBoard.update({"low-M": "X"})
            printBoard(theBoard)
        if inputX == 'low-R':
            theBoard.update({"low-R": "X"})
            printBoard(theBoard)


def handleInputO():
    inputX = input("\nPlayer 2 go, you may type in this format 'top-L', 'mid-L', 'low-L': ")
    if playerTurn == 2:

        if inputX == 'top-L':
            theBoard.update({'top-L': 'O'})

        if inputX == 'top-M':
            theBoard.update({"top-M": "O"})
        printBoard(theBoard)
        if inputX == 'mid-R':
            theBoard.update({"top-R": 'O'})
        if inputX == 'top-R':
            theBoard.update({"top-R": "O"})
            printBoard(theBoard)
        if inputX == 'mid-L':
            theBoard.update({"mid-L": "O"})
            printBoard(theBoard)
        if inputX == 'mid-M':
            theBoard.update({"mid-M": "O"})
            printBoard(theBoard)
        if inputX == 'mid-R':
            theBoard.update({"mid-R": "O"})
            printBoard(theBoard)
        if inputX == 'low-L':
            theBoard.update({"low-L": "O"})
            printBoard(theBoard)
        if inputX == 'low-M':
            theBoard.update({"low-M": "O"})
            printBoard(theBoard)
        if inputX == 'low-R':
            theBoard.update({"low-R": "O"})
            printBoard(theBoard)


# printBoard and theBoard code from https://medium.com/@pk1288780/creating-tic-tac-toe-in-python-using-dictionaries
# -70ab8ab49a19


while playerDidWin != True:
    handleInputX()
    print(playerTurn)
    playerTurn += 1
    print(playerTurn)
    handleInputO()
    print(playerTurn)
    playerTurn -= 1
    print(playerTurn)
    if theBoard['top-L'] == "X" and theBoard['top-M'] == "X" and theBoard['top-R'] == "X":
        playerDidWin = True

if playerDidWin == True:
    print("Player ", playerTurn, " has won!")
# print("You are Player 2 which is O.\nGrids are A1-A3, B1-B3, C1-C3")
# input("Player 2 go, you may type in this format 'top-L', 'mid-L', 'low-L': ")


# printBoard(theBoard)
