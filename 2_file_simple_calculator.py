print("~~~~~~~~~~Mini Caclutor~~~~~~~~~")
num1 = float(input ("enter first number here:"))
num2 = float (input("enter second number here:"))


print("press 1 for addition \ npress 2 for subtraction \ npress 3 for multiplication \ npress 4 for division")

choice = int (input ("enter yur choice from 1-4"))

if choice == 1: 
    print (num1 + num2 )

if choice == 2:
    print (num1  - num2 ) 


if choice == 3: 
    print (num1 * num2) 


if  choice ==4:
    print (num1 % num2 ) 


else: 
    print ("invalid input ")           