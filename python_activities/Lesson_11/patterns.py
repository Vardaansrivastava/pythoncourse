# Pattern: The repeated or systematic way in which something take splace is called a Pattern.
# Few Pattern Shapes Examples:
# 1.Simple Number Triangle Pattern, 
# 2. Inverted Triangle Pattern, 
# 3. Half Pyramid Pattern, etc.

# Example for Pattern:

for i in range(5): 
    for j in range(i+1): 
        print(i, end=" ")
    print() #prints a empty line

# Activity 1: Write a program to demonstrate a right angle triangle pattern using "*"?
for i in range(6)

# Activity 2:  Write a program to demonstrate a Floyd triangle pattern?
# 1) Take an integer input from the user and store it in `rows`.
#    (This represents the total number of rows to print.)

# 2) Initialize `number = 1`.
#    (This is the starting value to be printed in Floyd's Triangle.)

# 3) Print a heading message: "Floyd's Triangle".

# 4) Use an outer loop to handle each row from 1 to `rows` (inclusive):
#    a) The current row number is `i`.

# 5) Use an inner loop to handle the numbers in each row:
#    a) For row `i`, print `i` numbers, so loop `j` from 1 to `i` (inclusive).
#    b) Print the current value of `number` on the same line using `end='  '`.
#    c) Increase `number` by 1 after printing so the next number continues in sequence.

# 6) After finishing each row, print a blank `print()` to move to the next line.

# Activity 3: Write a program to demonstrate the numbers in a diamond pattern?
# 1) Take an integer input from the user and store it in `rowSize`.
#    (This represents the total height of the diamond pattern.)

# 2) Decide how many rows the top half of the diamond should have:
#    a) If `rowSize` is even, set `halfDiamRow = rowSize/2`
#    b) If `rowSize` is odd, set `halfDiamRow = rowSize/2 + 1`
#    (This ensures the middle row is included in the upper half.)

# 3) Initialize `space = halfDiamRow - 1`.
#    (This controls leading spaces before printing numbers in the upper half.)

# 4) Print the upper half of the diamond:
#    a) Use an outer loop `i` from 1 to `halfDiamRow` (inclusive) for rows.
#    b) For each row:
#       i) Print `space` number of blank spaces using an inner loop.
#       ii) Decrease `space` by 1 after printing spaces.
#       iii) Set `num = 1` to start printing numbers from 1 in that row.
#       iv) Print `(2*i - 1)` numbers in the row using another inner loop:
#           - Print the current `num` without moving to the next line.
#           - Increase `num` by 1 after each print.
#       v) Print a newline to move to the next row.

# 5) Reset `space = 1` for the lower half of the diamond.
#    (Now spaces increase as we go downward.)

# 6) Print the lower half of the diamond:
#    a) Use an outer loop `i` from 1 to `halfDiamRow - 1` for rows.
#    b) For each row:
#       i) Print `space` number of blank spaces using an inner loop.
#       ii) Increase `space` by 1 after printing spaces.
#       iii) Set `num = 1` to start printing numbers from 1 in that row.
#       iv) Print `2*(halfDiamRow - i) - 1` numbers using an inner loop:
#           - Print the current `num` without moving to the next line.
#           - Increase `num` by 1 after each print.
#       v) Print a newline to move to the next row.

