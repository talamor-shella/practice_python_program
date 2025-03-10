#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers

#empty list 
numbers = []

#for loop to make user input numbers ten times then append it to empty list
for i in range(10):
    user_input = int(input(f"Enter a number {i+1}: "))
    numbers.append(user_input)

#assign the first number to first index
first_number = numbers[0]

#get the sum of remaining numbers
sum1 = sum(numbers[1:])

#first number - sum of remaining numbers
result = first_number - sum1

#prints the result of first number - sum1
print(f"The result is: {result}")