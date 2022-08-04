import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = int(input("guess a number between 1 and 10: "))
   

    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")