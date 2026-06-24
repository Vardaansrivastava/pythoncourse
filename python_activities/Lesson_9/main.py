# While loop:
# The while loop repeatedly executes a code block while a particular condition is True and if the codition is False, it stops execution.
# The while loop works when the number of repetitions is not known.
# Infinite loop is when a condition never becomes false.
# Syntax:
# while (condition):
#     # Block of statement

# Example:

# i=1
# print("While loop: ")
# while i<6:
#     print(i)
#     i+=1

# print("For loop: ")
# for i in range(5):
#     print(i)

# Example for infinite loop:
# i=1
# while True:
#     print(i)
#     i+=2



# Activity 1:
# 1) Ask the user to enter the number of terms and store it in `n`.

# 2) Initialize `sum` to 0.
#    (This will store the running total.)

# 3) Initialize `i` to 1.
#    (This is the first number we will add.)

# 4) Repeat while `i` is less than or equal to `n`:
#    a) Add `i` to `sum`.
#    b) Increase `i` by 1 to move to the next number.

# 5) After the loop ends, print the final value of `sum`.


n = int(input("Enter a number :"))
sum = 0
i = 1
while i<=n:
    sum+=i
    i+=1
print(sum)


# Activity 2:
# 1) Set `i` to 0.

# 2) Start a loop that keeps running as long as `i` is less than or equal to 0.

# 3) Inside the loop, print: "I WILL RUN FOREVER"

# 4) Notice: `i` is never changed inside the loop.
#    That means `i` stays 0 forever, so the condition (i <= 0) stays true forever.
#    So the loop never stops (infinite loop).
i=0
while i<=0:
  print("I WILL RUN FOREVER")


# Activity 3:
# 1) Ask the user to enter a number and store it in `num`.

# 2) Set `sum` to 0.
#    (This will store the total of the cubes of each digit.)

# 3) Copy `num` into `temp`.
#    (We will change `temp` while checking digits, but we must keep `num` unchanged.)

# 4) Repeat while `temp` is greater than 0:
#    a) Find the last digit of `temp` and store it in `digit`.
#    b) Add (digit × digit × digit) to `sum`.
#    c) Remove the last digit from `temp` so you can move to the next digit.

# 5) After the loop, compare `num` and `sum`:
#    - If they are the same, print: `num` is an Armstrong number.
#    - Otherwise, print: `num` is not an Armstrong number.

num = int(input("Enter a number :"))
sum = 0
temp = num
while temp>0:
    digit = temp%10
    sum += digit**3
    temp //= 10
if num == sum:
    print(num, " is an armstrong number")
else:
    print(num, " is not an armstrong number")
