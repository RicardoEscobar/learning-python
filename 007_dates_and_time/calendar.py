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
for name in calendar.month_name:
  print (name)

for day in calendar.day_name:
  print (day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print ("Team meetings will be on:")
for month in range(1,13):
  # returns an array of weeks that represent the month
  calendar_object = calendar.monthcalendar(2019, month)
  # The first Friday has to be within the first two weeks
  weekone = calendar_object[0]
  weektwo = calendar_object[1]
   
  if weekone[calendar.FRIDAY] != 0:
    meetday = weekone[calendar.FRIDAY]
  else:
    # if the first friday isn't in the first week, it must be in the second
    meetday = weektwo[calendar.FRIDAY]
      
  print ("%10s %2d" % (calendar.month_name[month], meetday))
