# Making a calculator that adds, subtracts, multiplies and divides two numbers
x = float(input("Enter first number : "))
y = float(input("Enter second number : "))
print("select operation to perform : ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1/2/3/4) : ")
if choice == '1':
    print(x, "+", y, "=", x + y, "Thanks for using the calculator!", "'by Vardaan'")
elif choice == '2':
    print(x, "-", y, "=", x-y, "Thanks for using the calculator!", "'by Vardaan'")
elif choice == '3':
    print(x, "*", y, "=", x*y, "Thanks for using the calculator!", "'by Vardaan'")
elif choice == '4':
    print(x, "/", y, "=", x/y, "Thanks for using the calculator!", "'by Vardaan'" )
else:
    print("Invalid input")

