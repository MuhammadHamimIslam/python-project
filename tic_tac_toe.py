import random

# take user input 
def take_input(board): 
    if not is_board_full(board): 
        while True:
            try:
                turn = int(input("Enter your input (1-9): ").strip()) - 1
                if board[turn] != " ": 
                   raise ValueError
                break
            except (ValueError, IndexError):
                print("Invalid! Enter a number from 1–9 for an empty cell.")
        board[turn] = "×"
        if winner(board):
            print_board(board)
            return True
        if is_board_full(board): 
            return False
        ai_turn(board)
        print_board(board)
        if winner(board): 
            return True
    return False 

# AI's move 
def ai_turn(board): 
    while True: 
        ai_turn = random.randint(0, 8)
        if board[ai_turn] == " ": 
            board[ai_turn] = "O"
            break
    
# print the board
def print_board(board): 
    print(f"""
 {board[0]} | {board[1]} | {board[2]} 
-----------
 {board[3]} | {board[4]} | {board[5]}
-----------
 {board[6]} | {board[7]} | {board[8]}
    """)

# check if board is full 
def is_board_full(board): 
    return " " not in board

# check for winner 
def winner(board): 
    win_moves = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for move in win_moves: 
        if board[move[0]] == board[move[1]] == board[move[2]] != " ":
            winned = "Player" if board[move[0]] == "×" else "AI"
            print(f"{winned} wins!")
            return True
    return False

# game play 
def play_game(board):
    print_board([x+1 for x in range(9)])
    while not is_board_full(board):
        if take_input(board): 
            return 
    print("Tie!")

# play the game
def main():
    while True: 
        choice = input("Play a round? (y/n): ").strip().lower()
        if choice == "y":
            board = [" "] * 9 # the board
            play_game(board)
        elif choice == "n":
            print("Game ended!")
            break
        else:
            print("Invalid input!")

if __name__ == '__main__':
    main()