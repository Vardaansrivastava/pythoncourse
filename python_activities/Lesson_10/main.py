#  Nested Loop:
#  A loop inside another loop is called nested loop.
#  The first loop is called as Outer loop. The loop which is written inside the first loop is called inner loop.
# The outer loop can contain multiple inner loops. There is no limitation.
# The outer loop controls how many iterations the inner loop will perform.
# For each repetition of an outer loop, the inner loop re-starts and completes its execution.
# Nested loops are typically used for working with multidimensional data structure, suc as 2-D array.

# Syntax of nested while loop:
# while expresion:
#     while expression:
#         statements
#     statements

# Example of nested while loop:

# i=1
# while i<=5:
#     j=1
#     while j<=10:
#         print(j, end="")
#         j=j+1
#     print() #print(): it will print us a blank line.
#     i=i+1
    

# Syntax for nested for loop:
# for element in sequence:
#     for element in sequence:
#         body of inner loop
#     body of outer loop

# Example for nested for loop:
# for i in range(1,5):
#     for j in range(1,11):
#         print(j, end="")
#     print()

# Activity 1:
# 1) Ask the user to enter a word and store it in `string`.

# 2) Ask the user to enter a single character and store it in `char`.

# 3) Set `i` to 0.
#    (This will be used as the index to move through the string.)

# 4) Set `count` to 0.
#    (This will store how many times `char` appears.)

# 5) While `i` is less than the length of `string`:
#    a) Check if the character at position `i` in `string` is equal to `char`.
#    b) If yes, increase `count` by 1.
#    c) Increase `i` by 1 to move to the next character.

# 6) After the loop, print how many times `char` occurred in `string` using `count`.


string = input("Enter a word :")
char = input("Enter a single character :")
i = 0
count = 0
length = len(string)
while i<length:
    if string[i]==char:
        count+=1
    i+=1
print("This particular",char, "has occured", count, "times")



# Activity 2:
# 1) Take two integer inputs from the user and store them in `lower` and `upper`.
#    (These represent the starting and ending range.)

# 2) Print a message showing the range: from `lower` to `upper`.

# 3) Use a loop to check every number `num` from `lower` to `upper` (inclusive).

# 4) For each `num`, first check if it is greater than 1.
#    (Because prime numbers are always greater than 1.)

# 5) If `num` is greater than 1, test if it is prime:
#    a) Try dividing `num` by every number `i` from 2 to `num - 1`.
#    b) If `num` is divisible by any `i` (remainder is 0), it is NOT prime → stop checking (break).

# 6) If the loop finishes without finding any divisor (no break happened),
#    then `num` is prime → print `num`.

# Activity 3:
# 1) Take an integer input from the user and store it in `num`.
#    Also copy the same value into `t` for digit counting.

# 2) Initialize `numLen = 0` to count the number of digits.

# 3) Count the digits using a loop:
#    a) Repeat while `t > 0`
#    b) Increase `numLen` by 1 each time
#    c) Remove the last digit of `t` using `t = int(t/10)`

# 4) Check if the number has at least 4 digits:
#    If `numLen >= 4`, continue to find the middle digits.
#    Otherwise, print: "It's not a 4 or more than 4-digit number!"

# 5) If the number has 4 or more digits:
#    a) Set `numLen = int(numLen/2)` to locate the middle positions
#    b) Initialize `chk = 0` to track the digit index while extracting digits

# 6) Extract digits from right to left:
#    a) Repeat while `num > 0`
#    b) Get the last digit using `rem = num % 10`
#    c) If `chk == numLen`, store this digit as `midOne`
#    d) Else if `chk == (numLen - 1)`, store this digit as `midTwo`
#    e) Remove the last digit using `num = int(num/10)`
#    f) Increase `chk` by 1

# 7) Multiply the two middle digits:
#    `prod = midOne * midTwo`

# 8) Print the product in the required format:
#    "Product of Mid digits (midOne * midTwo) = prod"


