# Example file for working with classes

class myClass():
    def method1(self):
        print("myClass method")

    def method2(self, someString):
        print("myClass method2: " + someString)

def main():
    # Instantiates an object of "myClass" class
    classObject = myClass()
    classObject.method1()
    classObject.method2("This is a string")

if __name__ == "__main__":
    main()