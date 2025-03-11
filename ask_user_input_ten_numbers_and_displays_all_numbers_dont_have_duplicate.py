#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate

#make an empty list
numbers = []

#for loop that makes a user input ten numbers 
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    
#append it to empty list 
#for loop and if statement 