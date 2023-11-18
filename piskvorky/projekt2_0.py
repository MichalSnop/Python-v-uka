"""
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