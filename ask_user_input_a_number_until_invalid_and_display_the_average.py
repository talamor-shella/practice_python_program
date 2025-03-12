#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

#try-except and while loop
try:
    while True:
        num = int(input("Enter a number: "))
except ValueError:
    print("Invalid")
#empty list
#append user input in list
#get the sum
# result of sum divide to len of list