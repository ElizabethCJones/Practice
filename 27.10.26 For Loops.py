#A teacher asks you to create a program that helps students practice multiplication. 
# The program should display the multiplication tables for numbers 1 through 5. 
# Each table should list the products of the number with every number from 1 to 5. 
# After completing the table for one number, the program should clearly separate it from the next number’s table.
#Write a Python program using nested for loops to achieve this. Expected output

for number in range(1, 6):  
    print(f"{number} Times Tables: ")
    for i in range(1, 6): 
        print(f"{number} x {i} = {number * i}")
    print("-" * 10)


