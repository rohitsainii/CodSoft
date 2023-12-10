import tkinter as tk
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(player_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"You chose {player_choice.capitalize()} - Computer chose {computer_choice.capitalize()}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

root.geometry("400x300")  # Set a larger window size

choices = ['rock', 'paper', 'scissors']

def player_choice_rock():
    play_game('rock')

def player_choice_paper():
    play_game('paper')

def player_choice_scissors():
    play_game('scissors')

# Buttons for player's choices
rock_button = tk.Button(root, text="Rock", command=player_choice_rock)
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=player_choice_paper)
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=player_choice_scissors)
scissors_button.pack(pady=10)

# Display result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
