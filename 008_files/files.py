# Read and write files using the built-in Python file methods


def main():  
    # Open a file for writing and create it if it doesn't exist
    file_object = open("text_file.txt", "w+")

    # Open the file for appending text to the end
    for loop_counter in range(10):
        file_object.write("This is line: " + str(loop_counter) + "\r\n")

    # write some lines of data to the file


    # close the file when done


    # Open the file back up and read the contents


if __name__ == "__main__":
    main()
