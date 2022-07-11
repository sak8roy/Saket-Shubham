1.
string=input("Enter the the string :")
print(string[::-1])
 

2.
x=int(input("Enter the minimum value :"))
y=int(input("Enter the maximum value: "))
num=int(input("Enter the number for divisibility check :"))
i=x
while i<=y:
    if i%num==0 :
        print(i)
    i+=1

3.
a=float(input("Enter the length of side:"))
b=float(input("Enter the length of side:"))
c=float(input("Enter the length of side:"))
if a+b>c and a+c>b and b+c>a :
    s=(a+b+c)/2
    ar_tri=(s*(s-a)(s-b)(s-c))**(0.5)
    print(ar_tri)
else :
    print("Error")


4.
i=1
while i<=10:
	if(i<=5):
		j=1
		str=''
		while(j<=i):
			str=str+'*'
			j+=1
		print(str)
		i+=1
	else:
		j=10
		str=''
		while(j>i):
			str=str+'*'
			j-=1
		print(str)
		i+=1

5.
row=int(input("Enter the number of rows"))
n=0

for i in range(0,row+1):
      
      for j in range(i): 
            if n==26:
                n=0 
            else:
                pass
            y=chr(65+n) 
            print(y, end="")
            n+=1
      print("")



6.
lower_value = int(input("Enter the Lowest Range Value : "))  
upper_value = int(input("Enter the Upper Range Value : "))    
  
print ("The Prime Numbers in this range are : ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):                          
            if (number % i) == 0:                            
        else:  
            print (number)                                   



7.
accum=[]
for i in range(1,500):
    if i%7==0 and i%11==0 :
        accum.append(i)
print("The numbers divisible by 11 and are multiple of 7 are :",accum)        




8.
pos=[]
neg=[]
odd=[]
even=[]
times={}
li=[]
for i in range(10):
    num=int(input("Enter the number "))
    li.append(num)
    if num>=0:
        pos.append(num)
    elif num<0 :
        neg.append(num)
    if num%2==0 :
        even.append(num)
    else :
        odd.append(num)
    if num not in times :
            times[num]=1
    else:
        times[num]+=1
print("Positive numbers are: ",pos)
print("Negative numbers are: ",neg)
print("Even numbers are: ",even)
print("Odd numbers are: ",odd)
print("Number of times each number occurs in the List",times)




9.
n=int(input("Number of words: "))
li=[]
for i in range(n):
    word=input("Enter the word: ")
    li.append(word)
times={}
for i in li :
    if i not in times :
        times[i]=1
    else :
        times[i]+=1
print("Number of occurences: ",times)
