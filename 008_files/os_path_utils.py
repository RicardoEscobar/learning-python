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

    # Work with file paths


    # Get the modification time


    # Calculate how long ago the item was modified



if __name__ == "__main__":
    main()
