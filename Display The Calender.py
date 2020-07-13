#Program to display calendar of the given month and year

import calendar

yy = int(input("Enter the year "))
mm = int(input("Enter the month "))
print("\n********************************")
# display the calendar
print(calendar.month(yy, mm))
print("\n********************************")