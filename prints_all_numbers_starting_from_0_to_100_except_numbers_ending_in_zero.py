#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero

#for loop from 0 to 100
for i in range(0, 101):
    if i % 10 != 0: #checks numbers not ending with zero
        print (i)
    