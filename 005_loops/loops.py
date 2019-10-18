# Example file for working with loops

def main():
    number_x = 0

    # define a while loop
    while (number_x < 5):
        print(number_x)
        number_x = number_x + 1

    # define a for loop
    for number_x in range(5, 10):
        print(number_x)

    # use a for loop over a collection
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    for day in days:
        print(day)

    # use the break and continue statements
    for number_x in range(5, 10):
        if (number_x == 7): break
        print(number_x)

if __name__ == "__main__":
    main()