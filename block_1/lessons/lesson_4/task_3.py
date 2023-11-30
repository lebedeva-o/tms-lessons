number = 0

while number <= 100:
    print(number)
    answer = input("Should we break? (yes/no): ")

    if answer.lower() == "yes":
        break
    if answer.lower() == "no":
        number += 1
    else:
        print("Don't understand you")