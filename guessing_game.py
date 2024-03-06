#link to the flowchart:https://app.diagrams.net/#G1wYqAQQXeK43eH5xGMuWMcAvdVjPZ06Ap#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D


import random
import art1
#print(art1.logo())

print("\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
computer_number = random.randint(1,101)

game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if game_level == 'easy':
  attempts = 10
else:
  attempts = 5

def number_guess(attempts, computer_number):
  while attempts>0:
    print(f"You have {attempts} attempts remaining to guess the number")
    user_guess = int(input("Make a guess: "))
    if user_guess == computer_number:
      return print(f"You won! the number was {user_guess}")
    elif user_guess > computer_number:                      
      print("Too High")
    else:
      print("Too Low")
    attempts -=1
  return print(f"You Loose, the number was {computer_number}")

number_guess(attempts, computer_number)
