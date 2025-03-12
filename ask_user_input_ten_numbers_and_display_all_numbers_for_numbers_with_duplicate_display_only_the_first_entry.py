#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

#empty list 
numbers = []

#make user input ten numbers
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    
    #append the ten input numbers to empty list 
    numbers.append(num)

print(numbers)

#empty list to store all numbers and only the first entry
new_list = []

#for loop statement to display all numbers and first entry of with duplicate
for num in numbers:
   
   #checks if the num does not exist in new list
   if num not in new_list: 
       
       #prints the numbers not in new list 
       print(num) 

       #add it to new list 
       new_list.append(num)
       
    