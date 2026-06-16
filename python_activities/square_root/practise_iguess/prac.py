# WAP to create a user authentication system. if login is succesful than give the user access to the system otherwise show an error message. (use if-else statement)
username = input("Enter your username: ")
password = input("Enter your password: ")
# Predefined username and password
predefined_username = "Vardaan"
predefined_password = "IamVardaan"
# Check if the entered username and password match the predefined ones
if username == predefined_username and password == predefined_password:
    print("Login successful! Access granted to the system.")
else:
    print("Login failed! Invalid username or password. Access denied.")



# WAP to check if a seller has a profit or loss. The user should be able to input the cost price and selling price of an item, and the program should calculate and display whether there is a profit or loss, and the amount of profit or loss.
cost_price = float(input("Enter the cost price of the item : "))
selling_price = float(input("Enter the selling price of the item  : "))
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("The seller has a profit of ", profit ,"₹")
elif selling_price < cost_price:
    Loss = cost_price - selling_price
    print("The seller has a loss of ", Loss ,"₹")
else:
    print("There is no profit or loss. The seller broke even.")

