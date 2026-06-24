# WAP to calculate how many total digits are in a number entered by the user.Using while loop
number = int(input("Enter a number: "))
digit_count = 0

while number > 0:
    number //= 10
    digit_count += 1

print(f"The total number of digits in the entered number is: {digit_count}")