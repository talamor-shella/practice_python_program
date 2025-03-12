"""
Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. 
Display "Unique" after input when the inputted number don't have duplicate. 
Display "Duplicate" after input when the inputted number have duplicate.

"""
#empty list
num_list = []
 
#try and except statement
try:
    #while loop to continue asking user input until invalid 
    while True:
        num = int(input("Enter a number: "))
        num_list.append(num)
        
except ValueError:
    print("invalid")

#for checking the list users input 
print(num_list)

