#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

#ask user input a number 
number = (input("Enter a number: "))

#use zfill method
fill_zeros = number.zfill(6)

#print the number in 6 digit format
