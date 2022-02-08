#QUESTION 1

a=str(input("ENTER ANY STRING: "))
list=a.split() 
dict={} 
if list.__len__()==1:   
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")


#QUESTION 2

while(True):                 
    date=int(input("Enter The Date: "))
    if(1<=date<=31):
        break
    else:
        print("Please Enter A Valid Date")
while(True):                 
    month=int(input("Enter The Month: "))
    if(1<=month<=12):
        break
    else:
        print("Please Enter A Valid Month")
while(True):                
    year=int(input("Enter The Year: "))
    if(1800<=year<=2025):
        break
    else:
        print("Please Enter year from 1800 to 2025 only")
if(month==(1 or 3 or 5 or 7 or 8 or 10) ):    
    if(date==31):
        date=1
        month=month+1
        print(date,"/",month,"/",year)
    elif(date<31):
        date+=1
        print(date,"/",month,"/",year)
    else:
        print("PLEASE ENTER CORRECT DATE")

elif(month== (4 or 6 or 9 or 11) ):
    if(date==30):
        date=1
        month=month+1  
        print(date,"/",month,"/",year)   
    elif(date<30):
        date+=1
        print(date,"/",month,"/",year)
    else:
        print("PLEASE ENTER CORRECT DATE")       
elif(month== 2):
    if((year % 400 == 0) or  
    (year % 100 != 0) and  
    (year % 4 == 0)):   
        if(date==29):
            date=1
            month=month+1
            print(date,"/",month,"/",year)
        elif(date<29):
            date+=1
            print(date,"/",month,"/",year)
        else:
            print("PLEASE ENTER CORRECT DATE")
    else:
        if(date==28):
            date=1
            month+=1
            print(date,"/",month,"/",year)
        elif(date<28):
            date+=1
            print(date,"/",month,"/",year)
        else:
            print("PLEASE ENTER CORRECT DATE")
elif(month==12):
    if(date==31):
        date=1
        month=1
        year+=1  
        print(date,"/",month,"/",year)
    elif(date<31):
        date+=1;
        print(date,"/",month,"/",year)
    else:
        print("PLEASE ENTER CORRECT DATE")
    
else:
    print("PLEASE ENTER A CORRECT DATE")
print("\n")


#QUESTION 3

input_list = list(map(int, input("Enter a list of numbers: ").split()))

output_list = [(input_list[i], input_list[i]**2) for i in range(len(input_list))]

print("List: ",input_list)
print("Output: ",output_list)


#QUESTION 4

grade=int(input("ENTER YOUR GRADE BETWEEN 4 TO 10: "))
if(grade>10 or grade<4):
    print("PLEASE ENTER CORRECT GRADE")
elif(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")
print("\n")


#QUESTION 5

x = 6
for i in range(x):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='')  
    print()
print("\n")


#QUESTION 6

sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

while True:
    wish = input("Do you want to enter another student details(Y or N): ").upper()
    if wish == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif wish == 'N':
        break
    else:
     print('Invalid input!!!')

#a-part

print("a." ,students)

#b-part

print("b." ,{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#c-part

print("c." ,{k:v for k,v in sorted(students.items())})

#d-part

search = int(input("Please Enter SID Of The Student You Want To Search: " ))
print("d. Student With The Given SID Is: " ,students[search])


#QUESTION 7

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
terms=int(input("Enter The Number Of Terms In The Seires: "))
if (terms <= 0):    
   print("Plese enter a positive integer!")
else:
   print("Resultant Fibonacci sequence: ")
   sum=0
   for i in range(terms):
       print(fibo(i))
       sum=sum+fibo(i)
avg=float(sum/terms)
print("Average Of The Resultant Fibonacci Series = ",avg)


#QUESTION 8

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

# a part

A_Set = (Set1|Set2)-(Set1&Set2)
print("a. ", A_Set)

# b part

B_Set = (Set1|Set2|Set3) - ((Set1&Set2)|(Set2&Set3)|(Set3&Set1))
print("b. ", B_Set)

# c part

C_Set= ((Set1&Set2)|(Set1&Set3)|(Set3&Set2))-(Set1&Set2&Set3)
print("c. ",C_Set)

# d part

D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        D_Set.add(i)
print("d. ", D_Set)

# e part

E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        E_Set.add(i)
print("e. ", E_Set)