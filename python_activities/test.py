import random
secret = random.randint(1,50)
guess = int(input("Enter a number : "))
if guess > secret:
    print("Too high.")
elif guess < secret:
    print("too low.")
elif guess == secret:
    print("You win.")




    
