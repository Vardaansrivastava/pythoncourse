# Write a program to calculate the n number power of a given number. using for loop
number = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent (n): "))
result = 1
for _ in range(exponent):
    result *= number
print(f"The result of {number} raised to the power of {exponent} is: {result}")
