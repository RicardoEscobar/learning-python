# Example file for working with classes

class myClass():
    def method1(self):
        print("myClass method")

    def method2(self, someString):
        print("myClass method2: " + someString)

# Creates a child class that is based from "myClass"
class anotherClass(myClass):
    def method1(self):
        print("anotherClass method1")
    
    def method2(self, someString):
        print("anotherClass method2: " + someString)

def main():
    # Instantiates an object of "myClass" class
    classObject = myClass()
    classObject.method1()
    classObject.method2("This is a string")

    # Instantiates an object of "myClass" class
    anotherClassObject = anotherClass()
    anotherClassObject.method1()
    anotherClassObject.method2("This is another string")

if __name__ == "__main__":
    main()