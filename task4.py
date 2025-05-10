import random

user_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']

print(" Welcome to Neha's Rock-Paper-Scissors Game ")

while True:
    
    user_choice = input("\n Enter your choice (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print(" Invalid choice. Please enter rock, paper, or scissors.")
        continue

   
    computer_choice = random.choice(choices)
    print(f" Computer chose: {computer_choice}")

   
    if user_choice == computer_choice:
        print(" It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print(" You win this round!")
        user_score += 1
    else:
        print(" Computer wins this round!")
        computer_score += 1

    
    print(f"\n Scoreboard:\nNeha: {user_score} | Computer: {computer_score}")

    play_again = input("\n Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n Thanks for playing, Neha! See you next time!")
        break
