#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

#empty list 
numbers = []

#try-except and while loop to input number until invalid
try: 
    while True:
        num = int(input("Enter a number: "))

        #append the numbers in empty list
        numbers.append(num)
except ValueError:
    print("Invalid!")

# create list for duplicate
duplicate = []

#for loop 
for num in numbers:

    #checks the numbers with duplicates
    if numbers.count(num) > 1: 
        duplicate.append(num)

print(duplicate) #for checking only if duplicate numbers are in the list