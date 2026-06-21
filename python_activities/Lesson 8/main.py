# Loops:
# Types of loops: 
# 1. For loop : The for loop is used to repeat over a sequence.
# 2. While loop : Execute a statement while the given code is True.
# 3. Nested loop : We can operate multiple loops inside another while ofor loop.

# Example (For loop):
# For string
# n="hellofc"
# for i in n:  #i="h","e","l","l","o"
#     print(i)

# # For range
# for i in range(1,5): #i=0 #range(start,ending,steps)
#     print(i)


# Activity 1:

# 1) Ask the user to enter a number and store it in `n`.

# 2) Set `sum` to 0.
#    (This will store the running total.)

# 3) Use a `for` loop from 1 to `n` (inclusive):
#    - In each step, add the current value of `i` to `sum`.

# 4) After adding, print the current value of `sum`.
#    (So the user can see how the sum increases step by step.)

#Activity 2:

# 1) Ask the user to enter a word or sentence and store it in `string`.

# 2) Create an empty string called `string2`.
#    (This will store the reversed version.)

# 3) Loop through each character `i` in `string`:
#    - Add the character `i` in front of `string2`
#    - This builds the reversed string step by step.

# 4) Print the original string (`string`).

# 5) Print the reversed string (`string2`).

#Activity 3:

# 1) Ask the user to enter a number (greater than 1) and store it in `n`.

# 2) Print a message saying you will display numbers from `n` down to 1.

# 3) Use a `for` loop that starts from `n`, goes down to 1, and decreases by 1 each time.

# 4) Inside the loop, print the current value of `i` (so numbers appear in reverse order).




# Activity 3:
n = int(input("Enter a number : "))
print("I will display numbers from 'n' down to 1")
i=0
for i in range(n,0,-5): #for(i=8;i>=0;i-=1)
    print(i)
    



# Activity 2:
string = input("Input a word or  string :")
string2 = ""
for i in string:
    string2 = i+string2
print(string2)
    


# Activity 1:
n = int(input("Enter a number for its sum: "))
sum=0
for i in range(1, n+1): 
  sum = sum+i
  print(sum)
