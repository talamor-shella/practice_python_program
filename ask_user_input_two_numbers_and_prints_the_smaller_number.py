#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number

#ask user input two numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

#use min() function to return the smallest value
smaller_number = min(num1, num2)

#prints the smallest number
print(f"The smaller number is: {smaller_number}")