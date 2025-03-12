#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate

#empty list
numbers = []

#for loop to make user input ten numbers
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    
    #adds the input numbers to the list
    numbers.append(num)

#stores duplicate numbers in a single variable
duplicate = set()

#loop through numbers
for num in numbers: 
    
    #checks numbers with duplicate
    if numbers.count(num) > 1:

        #adds duplicate
        duplicate.add(num)

#display the list of user inputs
print(f"Inputs: {numbers}")

#prints numbers with unique duplicate
print("Duplicates", duplicate)
        
