#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
#Try and Except function, ask user to input two numbers, prints the quotient
try: 
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a number: "))
    quotient = num1 / num2
    print(f"The quotient is: {quotient}")

except ZeroDivisionError:
    print("Can't divide a number by zero")