#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

#empty list

#try-except and while loop to make user input number until invalid 
try:
    while True:
        num = int(input("Enter a number: "))
except ValueError:
    print("Invalid")

#append the inputted numbers in empty list
#use sort