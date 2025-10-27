#A company wants to print a visual representation of its pyramid-shaped awards hierarchy. 
# The pyramid consists of stars (*), where the first row has 1 star, the second row has 2 stars, and so on, up to n rows.
#Write a Python program that:
#Accepts a positive integer n from the user (number of rows).
#Prints a left-aligned pyramid of stars using nested for loops.
#Each row should contain a number of stars equal to the row number.

rows = int(input("Enter amount of rows = "))

print("Pyramid Star Pattern") 

for i in range(0, rows):6
    for k in range(0, i + 1):
        print('*', end = ' ')
    print()