# Read and write files using the built-in Python file methods


def main():  
    # Open a file for writing and create it if it doesn't exist
    file_object = open("text_file.txt", "w+")

    # Open the file for appending text to the end
    file_object = open("text_file.txt", "a")

    # write some lines of data to the file
    for loop_counter in range(10):
        file_object.write("This is line: " + str(loop_counter) + "\r\n")

    # close the file when done
    file_object.close()

    # Open the file back up and read the contents
    file_object = open("text_file.txt", "r")
    if file_object.mode == 'r':
        #contents = file_object.read()
        file_lines = file_object.readlines()
        for text_line in file_lines:
            print(text_line)
        #print(contents)

if __name__ == "__main__":
    main()
