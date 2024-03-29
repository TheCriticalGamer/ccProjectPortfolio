def welcome_player():
    print("Welcome to Tic Tac Toe\n")


welcome_player()
PLAYER_TURN = 1
PLAYER_DID_WIN = False
print("You are Player 1, which is X.\nGrids are A1-A3, B1-B3, C1-C3")

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def p_board(board):
    """prints the playing board

    Args:
        board (Dictionary): this prints the dictionary 'theBoard', 
        and assigns keys and values as, 
        quadrants or sectors, to make ease of placement during runtime and coding placement
    """
    print("\n-=-=-=-=-=-=-=-=-=-=\n")
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def handle_input_x():
    """handles input of player 1
    """

    input_x = input(
        "\nPlayer 1 go, you may type in this format 'top-L', 'mid-L', 'low-L': ")
    if PLAYER_TURN == 1:
        if input_x == 'top-L':
            theBoard.update({'top-L': 'X'})
        if input_x == 'top-M':
            theBoard.update({"top-M": "X"})

        if input_x == 'top-R':
            theBoard.update({"top-L": 'X'})
        if input_x == 'top-R':
            theBoard.update({"top-R": "X"})

        if input_x == 'mid-L':
            theBoard.update({"mid-L": "X"})

        if input_x == 'mid-M':
            theBoard.update({"mid-M": "X"})

        if input_x == 'mid-R':
            theBoard.update({"mid-R": "X"})

        if input_x == 'low-L':
            theBoard.update({"low-L": "X"})

        if input_x == 'low-M':
            theBoard.update({"low-M": "X"})

        if input_x == 'low-R':
            theBoard.update({"low-R": "X"})


def handle_input_o():
    """handles input of player 2
    """
    player_turn = 2
    input_x = input(
        "\nPlayer 2 go, you may type in this format 'top-L', 'mid-L', 'low-L': ")
    if player_turn == 2:

        if input_x == 'top-L':
            theBoard.update({'top-L': 'O'})
        if input_x == 'top-M':
            theBoard.update({"top-M": "O"})

        if input_x == 'top-R':
            theBoard.update({"top-R": "O"})

        if input_x == 'mid-L':
            theBoard.update({"mid-L": "O"})

        if input_x == 'mid-M':
            theBoard.update({"mid-M": "O"})

        if input_x == 'mid-R':
            theBoard.update({"mid-R": "O"})

        if input_x == 'low-L':
            theBoard.update({"low-L": "O"})

        if input_x == 'low-M':
            theBoard.update({"low-M": "O"})

        if input_x == 'low-R':
            theBoard.update({"low-R": "O"})


# printBoard and theBoard code from
# https://medium.com/@pk1288780/creating-tic-tac-toe-in-python-using-dictionaries-70ab8ab49a19
def input_loop():
    """_handles the input loop
    """
    while not PLAYER_DID_WIN:
        handle_input_x()
        p_board(theBoard)
        handle_input_o()
        p_board(theBoard)


winPossibilities = {
    "Possibility1":
    theBoard['top-L'] == "X" and theBoard['mid-L'] == "X" and theBoard['low-L'] == "X",
    "Possibility2":
    theBoard['top-M'] == "X" and theBoard['mid-M'] == "X" and theBoard['low-M'] == "X",
    "Possibility3":
    theBoard['top-R'] == "X" and theBoard['mid-R'] == "X" and theBoard['low-R'] == "X",
    "Possibility4":
    theBoard['top-L'] == "X" and theBoard['top-M'] == "X" and theBoard['top-R'] == "X",
    "Possibility5":
    theBoard['mid-L'] == "X" and theBoard['mid-M'] == "X" and theBoard['mid-R'] == "X",
    "Possibility6":
    theBoard['low-L'] == "X" and theBoard['low-M'] == "X" and theBoard['low-R'] == "X",
    "Possibility7":
    theBoard['top-R'] == "X" and theBoard['mid-R'] == "X" and theBoard['low-R'] == "X",
    "Possibility8":
    theBoard['top-L'] == "X" and theBoard['mid-M'] == "X" and theBoard['low-R'] == "X",
    "Possibility9":
    theBoard['top-R'] == "X" and theBoard['mid-M'] == "X" and theBoard['low-L'] == "X"
}
