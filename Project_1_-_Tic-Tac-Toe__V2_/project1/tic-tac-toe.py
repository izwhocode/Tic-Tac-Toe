# A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turns inputting their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9

# import libraries
import unittest

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# Update the gameboard with the user input
def markBoard(position, mark):
    if position >= 1 and position <= 9 and board[position] == ' ':
        board[position] = mark
    else:
        print("Sorry! This spot has been taken, please select another number.")

# Print the game board as described at the top of this code skeleton
def printBoard(board):
    print("\n---------------------")
    print("Board coordination:")
    print("\n1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")
    print(f"\n{board[1]} | {board[2]} | {board[3]}")
    print("--+---+--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("--+---+--")
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("---------------------")

# Check for wrong input, this function should return True or False.
def validateMove(position):
    if position not in range(1, 10):
        print("\nInvalid position. Please enter an integer between 1 - 9.")
        return False
    if board[position] != ' ':
        print("\nSorry! This spot has already been taken, select another integer.")
        return False
    return True

# List out all the combinations of winning
winning_combinations = [
    [1, 2, 3],  # Row 1
    [4, 5, 6],  # Row 2
    [7, 8, 9],  # Row 3
    [1, 4, 7],  # Column 1
    [2, 5, 8],  # Column 2
    [3, 6, 9],  # Column 3
    [1, 5, 9],  # Diagonal from top-left to bottom-right
    [3, 5, 7]   # Diagonal from top-right to bottom-left
]

# Implement a logic to check if the previous winner just won
def checkWin(player):
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] == player:
            return True
    return False

# Implement a function to check if the game board is already full
def checkFull():
    for key in board:
        if board[key] == ' ':
            return False
    return True

# To reset the board 
def resetGame():
    global board, mark, gameEnded
    board = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
    }
    mark = 'X'
    gameEnded = False


#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

mark = "X"
gameEnded = False

while True:
    resetGame()
    while not gameEnded:
        printBoard(board)
        print(f"\n{mark} player's turn.")
        while True:
            try:
                position = int(input("\nEnter a number 1-9: "))
                if validateMove(position):  # Call validateMove first
                    markBoard(position, mark)  # Place the mark AFTER validation
                    # Check for a win
                    if checkWin(mark):
                        printBoard(board)
                        print(f"\nCongratulations! Player {mark} wins!")
                        gameEnded = True
                        break

                    # Check for a tie (outside the win check)
                    if checkFull():
                        printBoard(board)
                        print("\nIt's a tie!")
                        gameEnded = True
                        break
                    break  # Exit the loop if the input is valid
            except ValueError:
                print("\nInvalid input. Please enter an integer.")

        # Switch players (X and O)
        if not gameEnded:  # Only switch players if the game is still running
            mark = 'O' if mark == 'X' else 'X'

    # Ask if players want to restart the game
    restart = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if restart != 'yes':
        print("\nThank you for playing!")
        break

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
