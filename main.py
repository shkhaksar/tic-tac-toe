import numpy


# Draw the given board in terminal
def draw_board(board):
    b_size = len(board)  # Get Board Size
    for i in range((b_size * 2) + 1):
        if i % 2 == 0:
            for j in range(b_size):
                if j == 0:
                    print(" --- ", end="")
                elif j == b_size - 1:
                    print("--- ")
                else:
                    print("--- ", end="")
        else:
            for j in range(b_size + 1):
                if j == b_size:
                    print("|")
                else:
                    if game[int(i / 2)][j] == 1:
                        print("|", end=" X ")
                    elif game[int(i / 2)][j] == 2:
                        print("|", end=" O ")
                    else:
                        print("|", end=" - ")


# Game format => game = [[0, 0, 0],
#                        [0, 0, 0],
#                        [0, 0, 0]]
# Winner Format => 0 => No one wins yet
#                  1 => Player One wins
#                  2 => Player Two wins
#                 -1 => Draw - No mark space available
def check_winner(board):
    winner = 0

    # Check Rows
    for i in range(len(board)):
        row = set(board[i])
        if len(row) == 1:
            if board[i][0] == 1:
                winner = 1
            elif board[i][0] == 2:
                winner = 2

    # Check Columns
    t_game = numpy.transpose(board)
    for i in range(len(t_game)):
        row = set(t_game[i])
        if len(row) == 1:
            if t_game[i][0] == 1:
                winner = 1
            elif t_game[i][0] == 2:
                winner = 2

    # Check diagonal
    if board[1][1] != 0:
        if board[1][1] == board[0][0] == board[2][2]:
            if t_game[1][1] == 1:
                winner = 1
            elif t_game[1][1] == 2:
                winner = 2
        elif board[1][1] == board[0][2] == board[2][0]:
            if t_game[1][1] == 1:
                winner = 1
            elif t_game[1][1] == 2:
                winner = 2

    # Check if any space is available
    is_move_available = False
    for i in range(len(game)):
        if 0 in game[i]:
            is_move_available = True
    if not is_move_available and winner == 0:
        winner = -1

    return winner


# Validate User Input
def valid_mark(user_input: str, board, ):
    l_input = user_input.split(",")
    try:
        row = int(l_input[0]) - 1
        col = int(l_input[1]) - 1
    except ValueError:
        return False
    if row > len(board) or col > len(board) or board[row][col] != 0:
        return False
    return True


# Modify board base on user input (use validate function before using this)
def submit_mark(user_input, board, is_player_one_turn):
    l_input = user_input.split(",")
    try:
        row = int(l_input[0]) - 1
        col = int(l_input[1]) - 1
    except ValueError:
        return board
    if is_player_one_turn:
        board[row][col] = 1
    else:
        board[row][col] = 2
    return board


if __name__ == '__main__':
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    print("Welcome! Player One => X, Player 2 => O")
    draw_board(game)
    game_winner = 0
    is_player_one = True  # True for Player One (X), False For Player 2 (O)

    while game_winner == 0:
        if is_player_one:
            print("Player One Turn!")
        else:
            print("Player Two Turn!")
        player_input = input("Please Enter Your Move: Ex.: 2,3 \n")
        if not valid_mark(player_input, game):
            print("Your move is invalid, please try again")
            continue
        game = submit_mark(player_input, game, is_player_one)
        is_player_one = not is_player_one
        draw_board(game)
        game_winner = check_winner(game)

    print("___Player " + str(game_winner) + " Wins___")
