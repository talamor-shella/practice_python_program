#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

#for loop to input ten numbers 
odd_count = 0 
for i in range(10):
    user_input = int(input(f"Enter a number {i+1:}: "))
    if user_input % 2 != 0: #if statement to check if the number is odd 
        odd_count += 1 #counts the numbers of odd 

print (f"There are {odd_count} odd numbers.") 
