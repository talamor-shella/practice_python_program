#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

#try-except and while loop to continue asking until unvalid
try:
    while True:
        num = int(input("Enter a number: "))
except ValueError:
    print("Invalid!")
    
#empty number list
#append user input to the list
#sort the list from highest to lowest
