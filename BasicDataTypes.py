repeat = True
repeatCorrect = False

def ReadRepeatInput():
    repeatInput = input("Continue? (Y/N):")
    if repeatInput == "Y":
        return True
    elif repeatInput == "N":
        return False
    else:
        print("Invalid input!")
        return ReadRepeatInput()

while repeat: 
    x = input("Input first number: ")
    y = input("Input second number: ")
    action = input("Input desired action:\na for addition\ns for subtracton\ndiv for division\nmul for multiplication\nInput here: ")
    if action == "a":
        result = x + y
    elif action == "s":
        if  x>y : 
            result = x - y
        else: 
            result = y - x
    elif action == "div":
        result = x / y
    elif action == "mul":
        result = x * y

    print("The result is "+ result)
    repeat = ReadRepeatInput()
