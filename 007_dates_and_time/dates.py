# Example file for working with date information

# Imports 'datetime' library
from datetime import date, time, datetime

def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is: ", today)

    # print out the date's individual components
    print("Date componets: ", today.day, today.month, today.year)

    # retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday # is: ", today.weekday())

    ## DATETIME OBJECTS
    # Get today's date from the datetime class


    # Get the current time


if __name__ == "__main__":
    main()