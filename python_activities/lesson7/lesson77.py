# Nested Conditional Statements:
# 
# Nested Conditional If Statement:  It means that if statement inside if statement, there is no limit for stacking if inside if. Mainly used for making a series of decisions.
# Example 1:

# i=13

# if (i<=13):
#     if(i>15):
#         print("i is smaller than 15.")
#     if(i<13):
#         print("i is smaller than 13 also.")
#     else:
#         print("i is greater than 12 but smaller than 15")

# Nested if-else statement:It means that an if-else statement inside if-else, multiple statements can be nested inside another, only by the use of indentation we can figure out the level of nesting.

# Example 2:
# i=int(input("Enter any number between 1 to 25: "))

# if(i==0):
#     print ("Number is zero.")
# else:
#     if(i>0):
#         print("number is positive.")
#     else:
#         print("number is negative.")

# Activity 1:
# Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.

# Activity 2:
# Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.

# Activity 3:
# Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.


# Activity 1.
print("Do you want your ride to be with a car or a bike.?")
print("1. car")
print("2. bike")
user_input = input("select 1 for car and 2 for bike :")
if user_input == '1':
    print("A ride with car it is!")
    print("There are two categories to chose from:")
    print("1. sedan")
    print("2. SUV")
    i = input("Choose :")
    if i == '1':
        print("A sedan it is!.")
    else:
        print("A SUV it is!.")
elif user_input == '2':
    print("A ride with bike it is!")
    print("There are two categories to choose from:")
    print("1. scooter")
    print("2. motorcycle")
    z = input("Choose :")
    if z == '1':
        print("A scooter it is!")
    else:
        print("A motorcycle it is!")
else:
    print("Invalid option.")








# Activity 2.
medical_cause = input("Do you have a medical cause? (Y/N): ")
if medical_cause.upper() == 'Y':
    print("You are allowed to take the exam.")
else:
    attendance = float(input("Enter your attendance percentage: "))
    if attendance > 75:
        print("You are allowed to take the exam.")
    else:
        print("You are not allowed to take the exam due to low attendance.")






# Activity 3.
units = int(input(" Please enter Number of Units you Consumed : "))

# Check for units less than 50
if(units < 50):
    amount = units * 2.60 
    surcharge = 25 

# Check for units less than 100
elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

# Check for units less than or equal to 200
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45


# more than 200
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

total = amount + surcharge
print("\nElectricity Bill = %.2f"  %total)