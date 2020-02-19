"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

len_arg = len(sys.argv)

if len_arg == 1:
    print(calendar.month(datetime.now().year, datetime.now().month))
elif (len_arg == 2) and (1 <= int(sys.argv[1]) <= 12):
    month = int(sys.argv[1])
    print(calendar.month(datetime.now().year, month))
elif (len_arg == 3) and (1 <= int(sys.argv[1]) <= 12) and (int(sys.argv[2]) >= 0):
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    print(calendar.month(year, month))
else:
    print(f'Enter values in the terminal like "python 14_cal.py 12 2010", where "python 14_cal.py" calls the file that has the program, "12" is the month and should be an integer from 1 and 12 with 1 and 12 inclusive, "2010" is the year and is an integer greater than or equal to zero')