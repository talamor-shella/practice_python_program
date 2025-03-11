#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers

#ask user input two numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

#if statement for swapping numbers 
if num1 > num2:
    num1, num2 = num2, num1 #to check num1 is the smaller number

#for loop in ascending order

#print the numbers between the two numbers