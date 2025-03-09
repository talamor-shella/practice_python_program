#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

#Ask user to input two numbers
number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))

#Make a variable for determining the bigger number
bigger_num = max(number_1, number_2)

#prints the bigger number
print(f"The bigger number is: {bigger_num}")