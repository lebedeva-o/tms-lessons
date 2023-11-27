import random

number = random.randint(0, 100)
while True:
    user_number = int(input("Guess number: "))
    if user_number == number:
        print("Congratulations!")
        break
    elif user_number > 100:
        print("Invalid number entered")
    elif user_number < number:
        print("Incorrect, the number is bigger than the entered number")
    else:
        print("Incorrect, the number is less than the entered number")