# Example file for working with Calendars

# import the calendar module
import calendar

# create a plain text calendar
calendar_object = calendar.TextCalendar(calendar.MONDAY)
calendar_string = calendar_object.formatmonth(2019, 1, 0, 0)
print(calendar_string)

# create an HTML formatted calendar
html_calendar_object = calendar.HTMLCalendar(calendar.MONDAY)
calendar_string = html_calendar_object.formatmonth(2019, 1)
print(calendar_string)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for iterator in calendar_object.itermonthdays(2019, 8):
    print(iterator)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms


# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script: