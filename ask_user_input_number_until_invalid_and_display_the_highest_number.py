#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

#empty list
numbers = []

#try-except and while loop to keep user input number until invalid
try:
    while True:
        num = int(input("Enter a number: "))

        #append the user input in empty list
        numbers.append(num)
except ValueError: 
    print("Invalid!")

#variable that returns the highest number
highest_number = max(numbers)

#print the highest number in the list
