#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers

#set the even count to zero
even_count = 0

#for loop to make user input ten numbers
for i in range(10):
    numbers = int(input(f"Enter a number {i+1}: "))

    #if statement to check if the number is even 
    if i % 2 == 0:
        #even count += 1
        even_count += 1  
#print even_count
print (f"There are {even_count} even")