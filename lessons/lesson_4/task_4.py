import random

n = random.randint(1, 5)
while True:
    a = int(input("Guess number: "))
    if a == n:
        print("Great! You win!")
        break
    else:
        print("Try again")