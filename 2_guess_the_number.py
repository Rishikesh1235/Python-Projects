import random 
number = int(input("Enter the upper limit: "))

def guess(x):
    int_random = random.randint(1,x)
    guess = 0 
    while guess != int_random:
        guess = int(input(f"Enter the number between 1 and {x}: "))
        if int_random > guess:
            print("Sorry! Wrong guess, too low")
        elif int_random < guess: 
            print("Sorry! Wrong guess, too high")
    print(f"Yay! you have guessed the number {int_random} correctly!")
guess(number)