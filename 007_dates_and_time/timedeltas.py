# Example file for working with timedelta objects

from datetime import date, time, datetime, timedelta

# constant to avoid magic number
DAYS_IN_YEAR = 36

# construct a basic timedelta and print it
print(timedelta(days = 365, hours = 5, minutes = 1))

# print today's date
now = datetime.now()
print("today is: " + str(now))


# print today's date one year from now
print("One year from now it will be: " + str(now + timedelta(days = DAYS_IN_YEAR)))

# create a timedelta that uses more than one argument
print("In 3 days and 5 weeks, it will be " +
    str(now + timedelta(days = 3, weeks = 5)))

# calculate the date 1 week ago, formatted as a string
time_ago = datetime.now() - timedelta(weeks = 1)
time_ago_string = time_ago.strftime("%A %B %d, %Y")
print("One week ago it was: " + time_ago_string)

### How many days until April Fools' Day?
today = date.today()
april_fools_day = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if april_fools_day < today:
    print("April Fool's day already went by %d days ago" % ((today - april_fools_day).days))
    april_fools_day = april_fools_day.replace(year = today.year + 1)

# Now calculate the amount of time until April Fool's Day
time_to_april_fools_day = april_fools_day - today
print("It's just ", time_to_april_fools_day, "days until April Fool's day")

