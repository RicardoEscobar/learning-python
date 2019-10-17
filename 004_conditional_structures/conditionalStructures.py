# Example file for working with conditional statements

def main():
    x, y = 100, 100

    # conditional flow uses  if, elif, else
    if (x < y):
        string = "x is lesser than y"
    elif (x == y):
        string = "x is the same as y"
    else:
        string = "x is greater than y"

    print(string)

# conditional statements let you use "a if C else b"

if __name__ == "__main__":
    main()