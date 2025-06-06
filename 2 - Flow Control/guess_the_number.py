import random


number = random.randint(1,20)
print("I'm thinking of a number from 1 to 20.")
for i in range(1,7):
    print("Take a guess.")
    guess = int(input())
    if guess < number:
        print("Your gess is too low.")
    elif guess > number:
        print("Your guess is to high.")
    else:
        break

if guess == number:
    print(f"Good job! You guessed my number in {i} guesses!")