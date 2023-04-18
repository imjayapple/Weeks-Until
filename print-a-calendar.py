import calendar

# Define the month and the year
month = 4 # April
year = 2023

# Create a TextCalendar object with the week starting on Saturday
cal = calendar.TextCalendar(calendar.SATURDAY)

# Generate a calendar for the specified month and year
month_calendar = calendar.monthcalendar(year, month)

# Print the header
print()
print("This program will print one calendar month. \n")
print("Sun Mon Tue Wed Thu Fri Sat")

# Iterate through the month_calendar and print each week
for week in month_calendar:
    for day in week:
        if day == 0:
            print("  ", end=" ") # Print empty spaces for days not in the month
        else:
            print(f"{day:2}", end=" ") # Print the day formatted as a two-character string
        print(" ", end="") # Add a space between the days
    print() # Start a new line for the next week







# formatmonth(theyear, themonth, w=0, l=0)