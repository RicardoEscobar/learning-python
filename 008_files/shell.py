# Example file for working with filesystem shell methods

import os
from os import path
import shutil


def main():
    # make a duplicate of an existing file
    file_name = "text_file.txt"

    if path.exists(file_name):
        # get the path to the file in the current directory
        source = path.realpath(file_name)

        # let's make a backup copy by appending "bak" to the name
        destiny = source + ".bak"

        # copy over the permissions, modification times, and other info


        # rename the original file
        new_file_name = "new_text_file.txt"
        os.rename(file_name, new_file_name)

        # now put things into a ZIP archive


        # more fine-grained control over ZIP files


if __name__ == "__main__":
  main()
