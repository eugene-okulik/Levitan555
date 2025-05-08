import random

salary = int(input())
bonus = random.choice([True, False])

if bonus == True:
    sale = salary + random.randrange(1, 5000)
    print(f"{salary}, {bonus} - '${sale}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
