#Prog08: Create a program that ask the user to input their fullname. Print the number of characters in the input.

#ask user input
full_name = input("Enter your fullname: ").strip()

#use len method
char_count = len(full_name)

#print the user input
print(char_count)