
# Basic Rock Paper Scissors Game
# Name: Lis Reitmeyer
# Date: 2/20/26

import random

"""
main.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

import random
from rich.console import Console
from rich.text import Text

# Create a Console object for rich output
console = Console()

choices = ['rock', 'paper', 'scissors']
num_to_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}

def get_user_choice():
	"""Prompt the user for their choice and return 'rock', 'paper', or 'scissors'."""
	while True:
		user_input = console.input("[bold]Choose rock (1), paper (2), or scissors (3): [/bold]").strip().lower()
		if user_input in num_to_choice:
			user_choice = num_to_choice[user_input]
		else:
			user_choice = user_input
		if user_choice in choices:
			break
		else:
			console.print("[red]Invalid choice. Please try again.[/red]")
	return user_choice

def get_computer_choice():
	"""Randomly return 'rock', 'paper', or 'scissors'."""
	computer_choice = random.choice(choices)
	return computer_choice

def determine_winner(user_choice, computer_choice):
	"""Return 'user', 'computer', or 'tie' based on the choices."""
	if user_choice == computer_choice:
		result = "tie"
	elif (
		(user_choice == 'rock' and computer_choice == 'scissors') or
		(user_choice == 'paper' and computer_choice == 'rock') or
		(user_choice == 'scissors' and computer_choice == 'paper')
	):
		result = "win"
	else:
		result = "loss"
	
	return result

def print_round_result(user_choice, computer_choice, result):
	"""Print the choices and the winner of the round using rich colors."""
	console.print(f"[magenta]Computer chose: {computer_choice}[/magenta]")
	console.print(f"[magenta]You chose: {user_choice}[/magenta]")

	# Tells program which result to print
	if result == "tie":
		console.print("[blue]It's a tie![/blue]")
	elif result == "win":
		console.print("[bold green]You win this round![/bold green]")
	else:
		console.print("[bold red]Computer wins this round![/bold red]")

def main():
	"""Main function to run the game for 3 rounds and print the final result."""
	# Initializes scores to 0 and allows user to choose number of rounds
	user_score = 0
	computer_score = 0
	rounds = int(input("How many rounds would you like to play? (1-5): "))
	if rounds < 1:
		rounds = 1
	elif rounds > 5:
		rounds = 5
	else:
		rounds = rounds

	console.print("[bold cyan]Welcome to Rock, Paper, Scissors![/bold cyan]")
	console.print("[green]You can type 'rock', 'paper', 'scissors' or use 1 for rock, 2 for paper, 3 for scissors.[/green]")

	# Main game loop, runs functions and keeps score
	for round_num in range(1, rounds + 1):
		console.print(f"\n[bold yellow]Round {round_num} of {rounds}[/bold yellow]")
		user_choice = get_user_choice()
		computer_choice = get_computer_choice()
		result = determine_winner(user_choice, computer_choice)
		print_round_result(user_choice, computer_choice, result)
		if result == "win":
			user_score += 1
		elif result == "loss":
			computer_score += 1
	
	# End of game, reveals results and prints them with nice formatting
	console.print("\n[bold underline]Game Over![/bold underline]")
	console.print(f"[cyan]Your score: {user_score}[/cyan]")
	console.print(f"[magenta]Computer score: {computer_score}[/magenta]")

	# Tells the program which result to print
	if user_score > computer_score:
		console.print("[bold green]Congratulations, you win the game![/bold green]")
	elif user_score < computer_score:
		console.print("[bold red]Sorry, the computer wins the game.[/bold red]")
	else:
		console.print("[yellow]It's a tie game![/yellow]")

if __name__ == "__main__":
	main()
