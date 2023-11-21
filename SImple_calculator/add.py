#define the function needed: add, sub, mul, div
#print options to the user
#ask for values
#call the functio
#add a while loop to continue until the user wnarts to exit.

def add(x, y):
    answer = x + y
    print(f"{x} + {y} = {answer}")

def sub(x, y):
    answer = x - y
    print(f"{x} - {y} = {answer}")

def multiply(x, y):
    answer = x * y
    print(f"{x} * {y} = {answer}")

def div(x, y):
    answer = x / y
    print(f"{x} / {y} = {answer}")


while True:
    print("A. Addition")
    print("B. Substration")
    print("C. Multiplication")
    print("D. Division")
    print("E. (Exit")

    choice = input("What do you wnat to ddo?: ")

    if choice.lower() == "a":
        print("Addition")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        add(x, y)

    elif choice.lower() == "b":
        print("Substration")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        sub(x, y)

    elif choice.lower() == "c":
        print("Multiplication")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        multiply(x, y)

    elif choice.lower() == "d":
        print("Division")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        div(x, y)

    elif choice.lower() == "e":
        print("End of program")
        quit()