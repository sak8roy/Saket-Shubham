#1

n=int(input("Enter a number: "))
check=0
for i in range(1,int(n/2)+1):
    if(n%i==0):
        check=check+i
if(n==check):
    print("Perfect number.")
else:
    print("Not a perfect number.")


#2


str=input("Enter a word: ")
str_rev=str[::-1]
if(str==str_rev):
    print("Palindrome.")
else:
    print("Not palindrome.")


#3


list=[1]
space="  "
rows=int(input("Enter the number of rows : "))
for i in range(rows):
    space=space+"   "
a=[]
for i in range(rows):
    a=[]  
    for k in list:
        a.append(k)
    print(space,list)
    for j in range(1,len(list)):
        list[j]=a[j-1]+a[j]
    list.append(1)
    space=space[:-2]


#4

i = input("enter your string : ")
i = i.replace(' ', '')
lst = set(i)
lst = list(lst)
#print(lst)

alphabets = 'qwertyuioplkjhgfdsazxcvbnm'
alphabets = list(alphabets)
#print(alphabets)


check = 0
for i in lst:
    if i in alphabets:
        check += 1


if check == len(alphabets):
    print('yes')
else:
    print('no')

#5

str=input("Enter the string: ")
words=str.split("-")
words=sorted(words)
for i in words:
    print(i,"\b-",end="")
print("\b ")


#6
class student_data:
    def _init_(self, name, branch):
        self.name = name
        self.branch = branch

    def student_id(self):
        print(f'name : {self.name} ||| branch : {self.branch}')


s = student_data('aniket', 'civil')
# function
s.student_id()

# arguments
print('--->', s.name)
print('--->', s.branch)



#7

class student():
    pass
class Marks():
    pass
student_1=student()
Marks_1=Marks()
print("The instance student_1 is a instance of class student : ",isinstance(student_1,student))
print("The instance student_1 is a instance of class Marks : ",isinstance(student_1,Marks))
print("The instance Marks_1 is a instance of class student : ",isinstance(Marks_1,student))
print("The instance Marks_1 is a instance of class Marks : ",isinstance(Marks_1,Marks))
print("The class student is a sub-class of of the built in object class : ",issubclass(student,object))
print("The class Marks is a sub-class of of the built in object class : ",issubclass(Marks,object))


#8
class sum():
    def __init__(self,list):
        self.list=list
    def py_1(self):
        l1=len(self.list)
        print(self.list)
        sum_list=[]
        for i in range(0,l1-2):
            for j in range(i+1,l1-1):
                for k in range(j+1,l1):
                    sum=self.list[i]+self.list[j]+self.list[k]
                    if(sum==0):
                        sum_list.append([self.list[i],self.list[j],self.list[k]])               
        return sum_list
list=[int(item) for item in input("Enter the numbers : ").split(",")]
a=sum(list)
print("The numbers which makes the sum equal to 0 are : ",a.py_1())



#9

class check():
    def __init__(self,str):
        self.str=str
 def myfunc(self):
            count=0
            for i in range(0,len(self.str)):
                if(i%2!=0):
                    if(self.str[i-1]=="(" and self.str[i]==")"):
                        pass
                    elif(self.str[i-1]=="[" and self.str[i]=="]"):
                        pass
                    elif(self.str[i-1]=="{" and self.str[i]=="}"):
                        pass
                    else:
                        count+=1

            if(count==0):
                return "valid."
            else:
                return "invalid."
str=input("Enter the set of parenthesis: ")
a=check(str)
print("The set of parenthesis is ",a.myfunc())


