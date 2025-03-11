#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate

#make an empty list
numbers = []

#for loop that makes a user input ten numbers 
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    
    #append it to empty list 
    numbers.append(num)

#gives the user lists of input numbers
print(numbers)

#for loop and if statement 
for num in numbers: 
    if numbers.count(num) == 1: #counts the numbers and checks the uniqueness of numbers
        
        #prints the numbers that dont have duplicate
        print(num)
if numbers.count(num) != 1: #if statement for all numbers that have duplicate
    print("All numbers have duplicate")