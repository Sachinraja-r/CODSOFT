import math

def create_board():
    return [' ']*9

def display_board(board):
    print()
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("--+---+--")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("--+---+--")
    print(board[6]+" | "+board[7]+" | "+board[8])
    print()

def player_move(board):
    pos = int(input("Choose a position (1-9): "))-1
    while board[pos] != ' ':
        pos = int(input("Position taken. Choose another (1-9): "))-1
    board[pos] = 'X'

def available_positions(board):
    return [i for i in range(9) if board[i]==' ']

def has_won(board, p):
    return ((board[0]==p and board[1]==p and board[2]==p) or
            (board[3]==p and board[4]==p and board[5]==p) or
            (board[6]==p and board[7]==p and board[8]==p) or
            (board[0]==p and board[3]==p and board[6]==p) or
            (board[1]==p and board[4]==p and board[7]==p) or
            (board[2]==p and board[5]==p and board[8]==p) or
            (board[0]==p and board[4]==p and board[8]==p) or
            (board[2]==p and board[4]==p and board[6]==p))

def board_full(board):
    return ' ' not in board

def minimax(board, ai):
    if has_won(board,'O'): return 1
    if has_won(board,'X'): return -1
    if board_full(board): return 0
    if ai:
        best = -math.inf
        for i in available_positions(board):
            board[i]='O'
            best = max(best,minimax(board,False))
            board[i]=' '
        return best
    else:
        best = math.inf
        for i in available_positions(board):
            board[i]='X'
            best = min(best,minimax(board,True))
            board[i]=' '
        return best

def ai_move(board):
    best_score=-math.inf
    best_pos=None
    for i in available_positions(board):
        board[i]='O'
        score=minimax(board,False)
        board[i]=' '
        if score>best_score:
            best_score=score
            best_pos=i
    board[best_pos]='O'

def game_loop():
    board=create_board()
    display_board(board)
    while True:
        player_move(board)
        display_board(board)
        if has_won(board,'X'):
            print("You win!")
            break
        if board_full(board):
            print("It's a draw!")
            break
        ai_move(board)
        display_board(board)
        if has_won(board,'O'):
            print("AI wins!")
            break

game_loop()
