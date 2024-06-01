# Write a Python program to display the current date and time.

from datetime import datetime

curren_date_time = datetime.now()
print(curren_date_time)

# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :

radius = float(input("enter the radius"))

area = 3.14 * radius * radius
print(area)

values = input("Input some comma-separated numbers: ")
list = values.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)
