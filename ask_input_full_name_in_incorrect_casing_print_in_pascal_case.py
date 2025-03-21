#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

#ask user input and use title() method
full_name = input("Enter your fullname: ").title()

#use replace method
pascal_case = full_name.replace(" ","")

#print the input in pascal case
print(pascal_case)