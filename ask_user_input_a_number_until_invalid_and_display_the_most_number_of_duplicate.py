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

#returns the duplicate list in ascending order
numbers.sort()
print(numbers)
#dictionary for counting recurrence of numbers in list
count_dup = {}

#for loop
for num in numbers:

    #adds one 
    if num in count_dup:
        count_dup[num] += 1
    else:
        count_dup[num] = 1
    




    
