#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

#empty list
numbers = []

#try-except and while loop to make user input number until invalid 
try:
    while True:
        num = int(input("Enter a number: "))
        
        #append the inputted numbers in empty listv
        numbers.append(num)
except ValueError:
    print("Invalid")

#use sort
numbers.sort(num)
