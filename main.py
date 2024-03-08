import sys


def welcome_player():
    print("Welcome to Tic Tac Toe\n")


welcome_player()
global PLAYER_TURN
PLAYER_TURN = 1
global PLAYER_DID_WIN
PLAYER_DID_WIN = False
print("You are Player 1, which is X.")

theBoard = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": " ",
}

#row1 = theBoard.zip(key in key, value in row1)

def p_board(board):
    """prints the playing board

    Args:
        board (Dictionary): this prints the dictionary 'theBoard',
        and assigns keys and values as,
        quadrants or sectors, to make ease of placement during runtime and coding placement
    """
    print("\n-=-=-=-=-=-=-=-=-=-=\n")
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


def handle_input_x():
    """handles input of player 1"""

    print(PLAYER_DID_WIN, "test 1", "it is now player", PLAYER_TURN)
    if PLAYER_TURN == 1:
        input_x = input(
            "\nPlayer 1 go, you may type in this format 'top-L', 'mid-L', 'low-L': "
        )
    if PLAYER_TURN == 1:
        if input_x == "top-L":
            theBoard.update({"top-L": "X"})
        if input_x == "top-M":
            theBoard.update({"top-M": "X"})
        if input_x == "q":
            # global PLAYER_DID_WIN
            # PLAYER_DID_WIN = True
            print("test")
        if input_x == "top-R":
            theBoard.update({"top-R": "X"})
        if input_x == "top-L":
            theBoard.update({"top-L": "X"})

        if input_x == "mid-L":
            theBoard.update({"mid-L": "X"})

        if input_x == "mid-M":
            theBoard.update({"mid-M": "X"})

        if input_x == "mid-R":
            theBoard.update({"mid-R": "X"})

        if input_x == "low-L":
            theBoard.update({"low-L": "X"})

        if input_x == "low-M":
            theBoard.update({"low-M": "X"})

        if input_x == "low-R":
            theBoard.update({"low-R": "X"})


def handle_input_o():
    """handles input of player 2"""
    global PLAYER_TURN

    print(PLAYER_DID_WIN, "test 2", "it is now player", PLAYER_TURN)
    if PLAYER_TURN == 2:
        input_x = input(
            "\nPlayer 2 go, you may type in this format 'top-L', 'mid-L', 'low-L': "
        )
    if PLAYER_TURN == 2:

        if input_x == "top-L":
            theBoard.update({"top-L": "O"})
        if input_x == "top-M":
            theBoard.update({"top-M": "O"})

        if input_x == "top-R":
            theBoard.update({"top-R": "O"})

        if input_x == "mid-L":
            theBoard.update({"mid-L": "O"})

        if input_x == "mid-M":
            theBoard.update({"mid-M": "O"})

        if input_x == "mid-R":
            theBoard.update({"mid-R": "O"})

        if input_x == "low-L":
            theBoard.update({"low-L": "O"})

        if input_x == "low-M":
            theBoard.update({"low-M": "O"})

        if input_x == "low-R":
            theBoard.update({"low-R": "O"})


# printBoard and theBoard code from
# https://medium.com/@pk1288780/creating-tic-tac-toe-in-python-using-dictionaries-70ab8ab49a19
def input_loop():
    """_handles the input loop"""
    global PLAYER_TURN
    while not PLAYER_DID_WIN and PLAYER_TURN == 1:
        
        handle_input_x()
        p_board(theBoard)
        win_check()
        PLAYER_TURN += 1
    
    while not PLAYER_DID_WIN and PLAYER_TURN == 2:
        
        handle_input_o()
        p_board(theBoard)
        win_check()
        PLAYER_TURN -= 1
        input_loop()

def win_check():
    """this checks if winner won"""
    global PLAYER_DID_WIN

    if theBoard["top-L"] == "X" and theBoard["top-M"] == "X" and theBoard["top-R"] == "X":
    
        PLAYER_DID_WIN = True
        if PLAYER_DID_WIN is True:
            print("\nPlayer 1 won\n")
    elif  theBoard["top-L"] == "O" and theBoard["top-M"] == "O" and theBoard["top-R"] == "O":
        PLAYER_DID_WIN = True
        if PLAYER_DID_WIN is True:
            print("\nPlayer 2 won\n")


def main():
    """main func"""
    input_loop()


if __name__ == "__main__":
    main()
