# Question 1 - PYTHON
A = input("Enter first number")
B = input("Enter second number")
C = input("Enter third number")
D = (int(A) + int(B) + int(C)) / 3
print("The average of three numbers =")
print(float(D))

# Question 2 - PYTHON
standard_deduction = 10000
dependent_deduction = 3000
gross = input("Enter the gross income")
No_of_dependents = input("Enter the number of dependents")
taxable_income = int(gross) - int(standard_deduction) - (int(dependent_deduction) * int(No_of_dependents))
tax = (float(taxable_income) * 0.2)
print("Your income tax is :")
print(float(tax))

# Question 3 - PYTHON
SID = input("Enter the SID")
Name = input("Enter the name")
Gender = input("Enter your Gender ")
Course_name = input("Enter the course name")
CGPA = float(input("Enter your CGPA"))
STUDENT = [SID, Name, Gender, Course_name, CGPA]
print(STUDENT)



# 04 Marks of students
s1=float(input("Enter the marks of Fist Student"))
s2=float(input("Enter the marks of Second Student"))
s3=float(input("Enter the marks of Third Student"))
s4=float(input("Enter the marks of Fourth Student"))
s5=float(input("Enter the marks of Fifth Student"))
slst=[s1, s2, s3, s4, s5]
slst.sort()
print(slst)

# 05
color=["Red", "Green", "White", "Black", "Pink", "Yellow"]
color.pop(3)
print(color)


color[3]="Purple"
print(color)









