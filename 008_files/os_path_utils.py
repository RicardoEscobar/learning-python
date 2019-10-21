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
    modification_timestamp = path.getmtime(file_name)
    
    print("Item path: " + str(path.realpath(file_name)))
    print("Item path and name: " + str(path.split(path.realpath(file_name))))

    # Get the modification time
    time_of_modification = time.ctime(modification_timestamp)
    print("Time of modification: " + time_of_modification)
    print(datetime.datetime.fromtimestamp(modification_timestamp))

    # Calculate how long ago the item was modified
    total_time = datetime.datetime.now() - datetime.datetime.fromtimestamp(modification_timestamp)
    print ("It has been " + str(total_time) + " since the file was modified")
    print ("Or, " + str(total_time.total_seconds()) + " seconds")


if __name__ == "__main__":
    main()
