board = [" " for i in range(9)]

#draws board
def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

#player move handler
def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    #checks if space is available
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is taken!")

#checks if certain spaces on the board are filled to see if victory has been achieved
def victory(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or\
      (board[3] == icon and board[4] == icon and board[5] == icon) or\
      (board[6] == icon and board[7] == icon and board[8] == icon) or\
      (board[0] == icon and board[4] == icon and board[8] == icon) or\
      (board[2] == icon and board[4] == icon and board[6] == icon) or\
      (board[1] == icon and board[4] == icon and board[7] == icon):
        return True
    else:
        return False

#if no more empty spaces, game ends in draw
def draw():
    if " " not in board:
        return True
    else:
        return False


while True:
    print_board()
    #player 1 move
    player_move("X")
    print_board()
    #checks if victory
    if victory("X"):
        print("Player 1 wins! Congrats!")
        break
    #checks if draw
    elif draw():
        print("Its a draw!")
        break
    #player 2 move
    player_move("O")
    #checks if victory
    if victory("O"):
        print_board()
        print("Player 2 wins! Congrats!")
        break
    #checks if draw
    elif draw():
        print("Its a draw!")
        break
