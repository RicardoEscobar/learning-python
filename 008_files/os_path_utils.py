# Example file for working with os.path module

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Refactor: declare variable to hold file name
    file_name = "text_file.txt"

    # Print the name of the OS
    print("Operative System: " + os.name)

    # Check for item existence and type
    print("Item exists: " + str(path.exists(file_name)))
    print("Item is a file: " + str(path.isfile(file_name)))
    print("Item is a directory: " + str(path.isdir(file_name)))

    # Work with file paths
    print("Item path: " + str(path.realpath(file_name)))
    print("Item path and name: " + str(path.split(path.realpath(file_name))))

    # Get the modification time
    time_of_modification = time.ctime(path.getmtime(file_name))
    print("Time of modification: " + time_of_modification)

    # Calculate how long ago the item was modified



if __name__ == "__main__":
    main()
