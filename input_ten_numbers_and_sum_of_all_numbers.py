#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers

#Make an empty list then use for loop to input ten numbers and append it to empty list
numbers = []

for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    numbers.append(num)

#prints the sum of ten numbers
sum_of_numbers = sum(numbers)
print(sum_of_numbers)
