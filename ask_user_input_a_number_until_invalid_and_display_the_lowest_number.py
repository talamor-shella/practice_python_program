#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

#make an empty list 
numbers = []

#try-except and while loop to continue asking until invalid
try: 
    while True:
        num = int(input("Enter a number: "))
        
        #append the users input in empty list
        numbers.append(num)
except ValueError:
    print("Invalid")

#displays the list of numbers inputted
print(f"Input numbers: {numbers}")

#variable that returns the lowest value
lowest_num = min(numbers)

#prints the lowest value


