# Python Challenges:
# PEDMAS: It stands for Parenthesis i.e. Brackets Exponentiation Division Multiplication Addition and Substraction.
# Example1:
# print(1+2**3) #9
# print(2*3**2) #18

# Expressions: Expressions are known as representation of values. They are different from statements, as statements do something while expressions represents a value.
# Example2:
# sum=5+3 # statement
# 5+3 # expression

# Logical Operators: AND , OR & NOT. 
# AND: If both conditons are True, the result is True.
# OR : If any one condition is True, the result is True.
# NOT : It reverses the value or response. 
# Example for AND:
# a=3
# n=5

# if(a<1 and n>6):
#     print("Hello")
# else:
#     print("See ya")

# # Example for OR:
# a=3
# n=5

# if(a<1 or n<6):
#     print("Hello")
# else:
#     print("See ya")

# # Example for NOT:

# a=3
# n=5

# if(not a<1 and n<6): #a<1 False: True n<6 True  (True and True)
#     print("Hello")
# else:
#     print("See ya")


#Activity 1:
# Write a program to understand how the operator precedence works.

# 1) Store values in `v`, `w`, `x`, `y`, and `z`.

# 2) Calculate the expression (v + w) * x / y and store the result back in `z`.

# 3) Print the value of `z` with a message.

# 4) Store a name in `name` and a number in `age`.

# 5) Check this condition using `or` and `and`:
#    - The code checks if `name` is "Alex"
#      OR (if `name` is "John" AND `age` is 2 or more).
#    - If the condition is true, print the welcome message.
#    - Otherwise, print the goodbye message.

# storing values.
v = 12
w = 17
x = 43
y = 2
z = (v + w) * x / y 
print("This is the answer! ", z)
name = "Vardaan"
age = 14
if(name == "Vardaan" and age >= 2):
    print("Welcome")
else:
    print("Goodbye")



