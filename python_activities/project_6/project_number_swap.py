# WAP for swapping three values
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
c = int(input("Enter the third value: "))
print("Before swapping: a =", a, "b =", b, "c =", c)
# Swapping the values
var = a
a = b
b = c
c = var
print("After swapping: a =", a, "b =", b, "c =", c)
# "var" is a random variable used to store the value of a temporarily while swapping.