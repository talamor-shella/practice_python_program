#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
#Try and Except statement for zero division error 
try: 
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

    #num1 // num2
    quotient = num1 // num2

    #prints the quotient without decimal point
    print(f"The quotient without decimal point is: {quotient}")
except ZeroDivisionError:
    print("Can't Divide a number by 0")
