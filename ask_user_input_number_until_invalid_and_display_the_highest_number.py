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

#displays the list of numbers the user inputted
print(f"Inputs: {numbers}")

#variable that returns the highest number
highest_number = max(numbers)

#print the highest number in the list
print(f"The highest number in the list is: {highest_number}")