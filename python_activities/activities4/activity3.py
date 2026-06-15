# take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

# calculating percentage of marks
sum = math+english+science+hindi
print("sum of math,english,science and hindi = ",sum)

percentage = (sum/400)*100

print(end="Percentage Mark = ")
print(percentage)