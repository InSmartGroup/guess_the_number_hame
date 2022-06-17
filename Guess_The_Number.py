import random
from sys import stderr

number_list = []
number = 0
lives = 0


def guessed_number():
    guess = random.choice(number_list)
    return guess


difficulty = input("Select difficulty. Type 'easy', 'normal', or 'hard': ").lower()
if difficulty == 'easy':
    number_list = list(range(1, 31))
    number = 30
    lives = 7
elif difficulty == 'normal':
    number_list = list(range(1, 51))
    number = 50
    lives = 7
elif difficulty == 'hard':
    number_list = list(range(1, 101))
    number = 100
    lives = 7
else:
    print("Please type 'easy', 'normal', or 'hard'.")

print("\nI'm thinking of a number. Try to guess it.")
print(f"It's in range from 1 to {number}.")
print(f"You've got {lives} attempts to guess it.")
number_guess = guessed_number()

while True:
    player_choice = int(input("\nWhat number do you think it is? "))
    if player_choice > number_guess:
        print("Too high!", file=stderr)
        lives -= 1
        print(f"You've got {lives} attempts remaining.")
    elif player_choice < number_guess:
        print("Too low!", file=stderr)
        lives -= 1
        print(f"You've got {lives} attempts remaining.")
    if player_choice == number_guess:
        print("You got it!", file=stderr)
        start_over = input("Would you like to play again? Type 'no' to quit: ").lower()
        if start_over == 'no':
            break
    if lives == 0:
        print("You're out of guess attempts. GAME OVER.")
        break

print("\nThank you for playing!")
