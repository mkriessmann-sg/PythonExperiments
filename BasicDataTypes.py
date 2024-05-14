repeat = True

def ReadRepeatInput():
    repeatInput = input("Continue? (Y/N):")
    if repeatInput == "Y":
        print("")
        return True
    elif repeatInput == "N":
        return False
    else:
        print("Invalid input!\n")
        return ReadRepeatInput()


def ReadNumberInput(type):
    try: 
        temp = int(input("Input %s number: " %type))
        print("")
    except ValueError:
        print("Invalid Input!\n")
        temp = ReadNumberInput(type)
    return temp

def PerformActions():
    action = input("Input desired action:\na for addition\ns for subtracton\ndiv for division\nmul for multiplication\nInput here: ")
    if action == "a":
        return x + y
    elif action == "s":
        if  x>y : 
            return x - y
        else: 
            return y - x
    elif action == "div":
        return x / y
    elif action == "mul":
        return x * y
    else: 
        print("Invalid input!\n")
        PerformActions()

while repeat: 
    x = ReadNumberInput("first")
    y = ReadNumberInput("second")
    result = PerformActions()
    print(result)
    print("The result is %s" %str(result))
    print("")
    repeat = ReadRepeatInput()

