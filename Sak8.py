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

# Question 4
marks = []
for i in range(5):  # for loop to take input 5 times
    marks.append(input("Enter marks of students"))
marks.sort()
print(marks)

# Question 5
colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colour.remove(colour[3])
print("Part a question : ", colour)
colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colour[3:5] = ['Purple']
print("Part b of question :", colour)









