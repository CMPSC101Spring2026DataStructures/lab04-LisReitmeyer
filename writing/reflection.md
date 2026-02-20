# Reflection: Rock, Paper, Scissors Lab

Name: Lis Reitmeyer
Date: 2/20/26

Please answer the following questions after you have completed the programming lab. Write your answers in complete sentences and provide thoughtful responses.

## Comprehension Questions

1. What is the purpose of breaking a program into functions? How did this help you in completing the lab?

Your Response:

Breaking a program into funcitons allows your code to be more efficient. In this lab we had "spaghetti code" which was very messy and all over the place. we were to use this code as a guideline of how to get our rock paper scissors program to work, but in a more organized way. Knowing how to split our code into functions was very important to completing this lab.


2. Describe how you validated user input in your version of the Rock, Paper, Scissors game. Why is input validation important?

Your Response:

In this game I validated user input with if/else statements. The first conditional statement checks if their input is either a number 1-3 or "rock" "paper" "scissors" 
The second conditional statement checks if their choice is valid or not. If their choice isn't valid it asks them to try again.

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

input validation is super important in coding because it makes sure the user inputs a valid choice. If the user inputs a non valid choice it could breal the program, causing more problems. 

3. How did you use comments and docstrings in your code? Give an example of a helpful comment or docstring you wrote.

Your Response:

I used comments to help explain what my code does.
Main.py has good examples of docstrings and comments. The docstring (provided) helps explain what the function does as a whole. The comment I added explains what that specific block of code is meant to do.

"""Main function to run the game for 3 rounds and print the final result."""
	# Initializes scores to 0 and allows user to choose number of rounds

4. Explain how the computer's move is generated in your program. What Python features did you use to accomplish this?

Your Response:

The computer's move is generated using the random function.

def get_computer_choice():
	"""Randomly return 'rock', 'paper', or 'scissors'."""
	computer_choice = random.choice(choices)
	return computer_choice

It is given a list of options that it can choose from, and then it returns its choice.

5. What was the most challenging part of refactoring the spaghetti code into a more structured program? How did you overcome this challenge?

Your Response:

The most challenging part was actually finding the code I needed that was lost im the spaghetti code. This challenge required me to understand the code and have the patience to sort through it. This really helped me understand how important code organization really is.

## Ethical Reflection Questions

1. Why is it important to write code that is easy for others to read and maintain? How does this relate to your responsibilities as a programmer?

Your Response:

This lab helped me understand just how important writing understandable code. I knew it was important before, but trying to untangle the spaghetti code took a while, and it could have been much easier if it was organized. Part of your responsiblity as a programmer is making sure that your code can easily be used and understood bu other people.

2. Consider the use of open source code (like the spaghetti code provided). What are some ethical considerations when using, modifying, or sharing code written by others?

Your Response:

Even if you are fixing it, it could technically still be plagirizarion if you are claiming it as yours without credit. Maybe that person dosen't want others to use their code like that with no permission. 

---

(Did you remember to add your name and date at the top of your reflection file?)
