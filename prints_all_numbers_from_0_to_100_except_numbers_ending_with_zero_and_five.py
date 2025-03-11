#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

#use for loop starting from 0 and stops to 100
for i in range(0, 100):

    # i % 10 != 0 and i % 5 != 0
    if i % 10 != 0 and i % 5 != 0:

        #prints the numbers except numbers ending in zero and five
        print(i)
