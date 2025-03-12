#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

#empty list
numbers =  []

#try-except and while loop
try:
    while True:
        num = int(input("Enter a number: "))

        #append user input in list
        numbers.append(num)
except ValueError:
    print("Invalid")


#get the sum
# result of sum divide to len of list