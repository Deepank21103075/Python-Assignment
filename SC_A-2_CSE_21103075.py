# QUESTION 1

string1="Python is a case sensitive language"
#a part
print("THE LENGTH OF STRING IS",len(string1)) 
#b part
print("THE REVERSED STRING IS ",string1[-1::-1])
#c part
string2=string1[10:26] 
#d part
string2.replace("a case sensitive","object oriented") 
#e part
print("THE INDEX OF SUBSTRING a is ",string1.find('a'))
#f part
print("THE ORIGINAL STRING AFTER REMOVING WHITESPACES IS",string1.replace(" ",""))
print("\n")

#QUESTION 2

NAME=input("ENTER YOUR NAME: ")
SID=int(input("ENTER YOUR SID: "))
DEPT=input("ENTER YOUR DEPARTMENT: ")
CGPA=float(input("ENTER YOUR CGPA: "))
print("Hey %s,"%NAME,"Here!")
print("My SID is %d" %SID)
print("I am from %s"%DEPT,"and my CGPA is %f"%CGPA)
print("\n")

#QUESTION 3

a=56
b=10
#a part
print("a. ",a&b)
#b part
print("b. ",a|b)
#c part
print("c. ",a^b)
#d part
print("Left shift both a and b with 2 bits respectively are :",a<<2 ,b<<2)
#e part
print("Right shift a with 2 bits and b with 4 bits respectively are : ",a>>2,b>>4)
print("\n")


#QUESTION 4

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("THE LARGEST NUMBER IS ",largest)
print("\n")


#QUESTION 5

s=input("ENTER A STRING: ")
if (s.find('name') != -1):
    print ("Yes")
else:
    print ("No")
print("\n")

#QUESTION 6

a=int(input("ENTER FIRST SIDE OF TRIANGLE: "))
b=int(input("ENTER SECOND SIDE OF TRIANGLE: "))
c=int(input("ENTER THIRD SIDE OF TRIANGLE: "))
if(a>(b+c)):
    print("No")
elif(b>(a+c)):
    print("No")
elif(c>(a+b)):
    print("No")
else:
    print("Yes")
print("\n")
