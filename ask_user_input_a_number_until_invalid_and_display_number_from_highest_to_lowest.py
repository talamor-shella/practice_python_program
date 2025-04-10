#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

#empty number list
numbers = []

#try-except and while loop to continue asking until unvalid
try:
    while True:
        num = int(input("Enter a number: "))

        #append user input to the list
        numbers.append(num)
except ValueError:
    print("Invalid!")

#sort the list from highest to lowest
numbers.sort(reverse=True)

print(f"Numbers from ighest to lowest: {numbers}")
