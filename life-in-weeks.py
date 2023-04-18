import calendar

year = int(input('Enter the year you were born: '))
month = int(input('Enter month you were born: '))
day = int(input('Enter day you were born: '))
birthdate = print(f'Your birthdate is {month} {day} {year}')

calendar.TextCalendar({year})
