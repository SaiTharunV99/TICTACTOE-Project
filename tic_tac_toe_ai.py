import math

def print_board(board):
    for row in board:
        print(row)
    print()

def check_winner(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True

    for col in range(len(board)):
        if all([board[row][col] == player for row in range(len(board))]):
            return True

    if all([board[i][i] == player for i in range(len(board))]):
        return True

    if all([board[i][len(board)-1-i] == player for i in range(len(board))]):
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def minimax(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ' ':
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ' ':
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ' ':
                board[i][j] = "O"
                score = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    size = 3
    board = [[' ' for _ in range(size)] for _ in range(size)]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player move
        row = int(input("Enter your move row (0-2): "))
        col = int(input("Enter your move column (0-2): "))

        if board[row][col] != ' ':
            print("Cell already occupied! Try again.")
            continue
        board[row][col] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = "O"

        print_board(board)

        if check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break

if __name__ == "__main__":
    main()