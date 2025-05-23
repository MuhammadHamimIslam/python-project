import random 

turns = ("rock", "paper", "scissor")

def play_game(): 
    bot_turn = random.choice(turns)
    while True:
        user_turn = input("Enter your turn: (rock, paper, scissor): ").strip()
        if user_turn in turns: break
        else:
            print("Invalid input!")
    print(f"Your turn: {user_turn}")
    print(f"Bot's turn: {bot_turn}")
    if user_turn.lower() == "rock": 
        if bot_turn == "rock": 
            print("It's a tie!")
        elif bot_turn == "paper":
            print("Bot wins!")
        else:
            print("You winned!")
    elif user_turn.lower() == "paper":
        if bot_turn == "paper": 
            print("It's a tie!")
        elif bot_turn == "rock":
            print("You winned!")
        else:
            print("Bot wins!")
    elif user_turn.lower() == "scissor":
        if bot_turn == "scissor": 
            print("It's a tie")
        elif bot_turn == "rock":
            print("Bot wins")
        else:
            print("You winned")

while True:
    choice = input("Do you want to continue?(y/n): ")
    if choice == "n": break
    elif choice == "y":
        play_game()
    else:
        print("Invalid choice!")