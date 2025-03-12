#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

#try-except and while loop to keep user input number until invalid
try:
    while True:
        num = int(input("Enter a number: "))
except ValueError: 
    print("Invalid!")
#create an empty list
#append user input in empty list
#variable that returns the highest number
#print the highest number in the list