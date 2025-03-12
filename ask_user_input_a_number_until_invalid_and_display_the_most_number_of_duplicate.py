#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

#empty list 
number = []

#try-except and while loop to input number until invalid
try: 
    while True:
        num = int(input("Enter a number: "))

        #append the numbers in empty list
        number.append(num)
except ValueError:
    print("Invalid!")

print(number) #for checking only if the input numbers are on the list

#for loop 

# create list for duplicate
