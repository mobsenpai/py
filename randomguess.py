import random
num = random.randint(1,100)
guess = int(input("Enter you guess: "))
while guess != num:
    guess = int(input("Wrong! try again: "))
print("You guessed right")
