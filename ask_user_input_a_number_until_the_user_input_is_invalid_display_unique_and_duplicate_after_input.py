"""
Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. 
Display "Unique" after input when the inputted number don't have duplicate. 
Display "Duplicate" after input when the inputted number have duplicate.

"""
#empty list
numbers = []

#try and except statement
try:
    #while loop to continue asking user input until invalid 
    while True:
        num = int(input("Enter a number: "))
        
        #checks if the numbers is not in the list 
        if num not in numbers: 
            
            #prints unique if not in the list
            print("Unique")

            #adds the input numbers to list
            numbers.append(num)
        
        #prints duplicate if number is already in the list
        else: 
            print("Duplicate")
except ValueError:
    print("Invalid")


