hlavicka = """
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Michal Snopko
email: michalsnopko84@gmail.com
discord: michalsn.
"""

def display_board(board):
    # Vypsání hrací plochy
    for row in board:
        print("+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+")

def check_winner(board, mark):
    # Kontrola výherních kombinací
    for row in board:
        if all([cell == mark for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == mark for row in range(3)]):
            return True
    if all([board[i][i] == mark for i in range(3)]) or all([board[i][2 - i] == mark for i in range(3)]):
        return True
    return False
def tic_tac_toe():
    print("Welcome to Tic Tac Toe")
    print("===========================================")
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("===========================================")
    print("Let's start the game")
    print("-------------------------------------------")

    board = [[" " for _ in range(3)] for _ in range(3)]
    display_board(board)

    current_mark = "X"
    
    for _ in range(9):
        while True:
            try:
                move = int(input(f"Player {current_mark} | Please enter your move number (1-9): "))
                row = (move - 1) // 3
                col = (move - 1) % 3

                if board[row][col] != " ":
                    print("This position is already taken. Try again.")
                    continue

                board[row][col] = current_mark
                break
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 9.")

        display_board(board)

        if check_winner(board, current_mark):
            print(f"Congratulations, the player {current_mark} WON!")
            return

        current_mark = "O" if current_mark == "X" else "X"

    print("It's a tie!")

# Spuštění hry
tic_tac_toe()

