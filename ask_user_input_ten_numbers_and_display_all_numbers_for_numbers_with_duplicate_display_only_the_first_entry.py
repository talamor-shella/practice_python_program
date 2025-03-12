#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

#empty list 
numbers = []

#make user input ten numbers
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    
    #append the ten input numbers to empty list 
    numbers.append(num)

print(numbers)

#for loop statement to display all numbers and first entry of with duplicate
for num in numbers:
    if numbers.count(num) > 1: 
        numbers.remove(num)
    print(num) #duplicates are not properly handed