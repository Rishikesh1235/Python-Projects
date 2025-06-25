import random 

def comp_guess(x):
    low = 1 
    high = x
    feedback = ' '
    while feedback != 'c':
        guess = random.randint(low,high)
        print(f"{guess}")
        feedback = str(input("Is the guess too High (h) or too Low (l) or correct(c): "))
        if feedback == 'h':
            high = guess + 1
        elif feedback == 'l':
            low = guess - 1
    
    print(f"Yay! Computer has guessed the number {guess} correctly!")

comp_guess(100)
            
    