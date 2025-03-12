#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

#make an empty list 

#try-except and while loop to continue asking until invalid
try: 
    while True:
        num = int(input("Enter a number: "))
except ValueError:
    print("Invalid")
#append the users input in empty list
#variable that returns the lowest value
#prints the lowest value

