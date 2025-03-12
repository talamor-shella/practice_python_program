#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate

#empty list
numbers = []

#for loop to make user input ten numbers
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    
    #adds the input numbers to the list
    numbers.append(num)

#if statement 
if numbers.count(num) > 1: 
    print(numbers)
