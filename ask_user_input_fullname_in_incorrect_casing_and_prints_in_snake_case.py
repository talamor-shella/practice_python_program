#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

#ask user input and use lower() method
full_name = input("Enter your fullname: ").lower()

#use replace() method
snake_case = full_name.replace(" ","_")

#print input in snake case
print(snake_case)