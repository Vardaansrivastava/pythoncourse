# WAP to check the entered age by the user is between 10 and 20 years or not. using nested conditional statements.
age = int(input("Enter your age: "))
if age >= 10:
    if age <= 20:
        print("Your age is between 10 and 20 years.")
    else:
        print("Your age is greater than 20 years.")
else:
    print("Your age is less than 10 years.")