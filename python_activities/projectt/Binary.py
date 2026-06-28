# WAP to convert a decimal number to binary number using nested while loop.
decimal = int(input("Enter a decimal number: "))
binary = ""
while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2
print("Binary number:", binary)
