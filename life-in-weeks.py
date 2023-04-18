# Author: Jay Apple
# Last Updated: April 18 2023

import calendar

year = int(input('Enter the year you were born: '))
month = int(input('Enter month you were born: '))
day = int(input('Enter day you were born: '))
birthdate = print(f'Your birthdate is {month} {day} {year}')

calendar.TextCalendar({year})



# How many days are there in this month?
# What is the starting day (0... 6, 0 is Sunday)?
#   Sun Mon Tue Wed Thu Fri Sat
#            1   2   3   4   5
#    6   7   8   9   10  11  12
#

for week in range(6): # week = 0, 1, 2, 3, 4, 5
    for day in range(7): # day = 0, 1, 2, 3, 4, 5, 6,
        print(dateCurrent)
        dateCurrent += 1


