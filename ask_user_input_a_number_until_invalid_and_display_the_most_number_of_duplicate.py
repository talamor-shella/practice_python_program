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

#returns the numbers list in ascending order
numbers.sort()

#displays the list of numbers in ascending order
print(numbers)

#dictionary for counting recurrence of numbers in list
recurrence = {}

#for loop
for num in numbers:

    if num in recurrence:
        recurrence[num] += 1 #increases count by one if it already exist in dictionary

    else:
        recurrence[num] = 1 #creates new entry if num does not exist in dictionary

most_recurrence = max(recurrence, key=recurrence.get) #to select the key with most recurrence in dictionary

print(f"The number with the most number of duplicate is: {most_recurrence}")

    




    
