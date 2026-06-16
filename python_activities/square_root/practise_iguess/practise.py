# WAP to check if the number is a perfect square or not. If it is a perfect square, then print the square root of the number. otherwise, print "Not a perfect square".
user_input = int(input("Enter a number to check if it is a perfect square or not :"))
root = int(user_input ** 0.5)
if root * root == user_input:
    print("The number is a perfect square. The square root of ", user_input, " is ", root)
else:
    print("Not a perfect square.")


# WAP to guess a random number between 1 and 100. The user should be able to input their guess and the program should give feedback on whether the guess is too low, too high, or correct. The program should continue until the user guesses the correct number.
import random
random_number = random.randint(1, 100)
guess = 0
while guess != random_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        