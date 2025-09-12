import random

turns = ["rock", "scissors", "paper"]

while True:
    turn_player_one = random.choice(turns)
    turn_player_two = input("Enter your turn, or type exit: ")
    
    if turn_player_two == "exit":
        print("Thanks for playing, bye bye!")
        break
    
    print(f"Player 1: {turn_player_one} vs. Player 2: {turn_player_two}")
    
    if turn_player_one == turn_player_two:
        print("draw")
    elif (turn_player_one == "rock" and turn_player_two == "paper") or \
        (turn_player_one == "scissors" and turn_player_two == "rock") or \
        (turn_player_one == "paper" and turn_player_two == "scissors"):
        print("player 2 wins!")
    else: 
        print("player 1 wins!")
