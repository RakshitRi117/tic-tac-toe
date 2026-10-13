import itertools
from colorama import Fore, Back, Style, init
init()

game = [['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']]

def game_board(game_map, row=0, colm=0, player='X'):
    if game_map[row][colm] != '.':
        print("That spot is already taken! Try again.")
        return False
    game_map[row][colm] = player
    return True

def display_board(game_map):
    print ("  0    1    2")
    print ("  --------------")
    for i, row in enumerate(game_map):
        formatted_row = " | ".join((Fore.RED + "X" + Style.RESET_ALL if cell == "X" 
                                                                    else Fore.GREEN + "O" + Style.RESET_ALL if cell == "O" 
                                                                    else " ") 
        for cell in row) # seperator '|' whihc seperates the list elements
        print(f"{i} | {formatted_row} |")
        print("  --------------")


def game_winner(game_map):
    n = len(game_map)

    # check rows
    for row in game_map:
        if row[0] != '.' and row.count(row[0]) == n:
            print("Winner by Row --> Player", row[0])
            return True

    # check columns
    for col in range(n):
        checkVertical = []
        for row in game_map:
            checkVertical.append(row[col])
        if checkVertical[0] != '.' and checkVertical.count(checkVertical[0]) == n:
            print("Winner by Column --> Player", checkVertical[0])
            return True

    # check right diagonal
    rightDiag = []
    for i in range(n):
        rightDiag.append(game_map[i][i])
    if rightDiag[0] != '.' and rightDiag.count(rightDiag[0]) == n:
        print("Winner by Right Diagonal --> Player", rightDiag[0])
        return True

    # check left diagonal
    leftDiag = []
    for i in range(n):
        leftDiag.append(game_map[i][n-i-1])
    if leftDiag[0] != '.' and leftDiag.count(leftDiag[0]) == n:
        print("Winner by Left Diagonal --> Player", leftDiag[0])
        return True

    return False

players = ['X', 'O']

play = 1
while play:
    play = int(input("Do you want to Play? 1 (YES) or 0 (NO): "))
    if play == 0:
        break

    display_board(game)   # show current board

    # cycle through players
    playerChoice = itertools.cycle(players)
    gameWon = False

    while not gameWon:
        current_player = next(playerChoice)
        print("Current Player:", current_player)

        # ask for move
        playRow = int(input("Enter row index (0,1,2): "))
        playColumn = int(input("Enter column index (0,1,2): "))

        # update board
        if not game_board(game, playRow, playColumn, current_player):
            continue  # invalid move, retry

        display_board(game)

        # check winner
        gameWon = game_winner(game)

        #draw check
        if not gameWon and all(all(cell!=0 for cell in row)for row in game):
            print("Game Draw")

    print("GAME OVER !")
    break
