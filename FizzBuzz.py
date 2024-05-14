
def inputNumber():
    try:
        return int(input("Please input number:"))
    except ValueError:
        print("Invalid input!")
        inputNumber()


number = inputNumber()

for x in range(1,number): 
    if x%3 == 0 and x%5 == 0:
        print("FizzBuzz")
    elif x%3 == 0:
        print("Fizz")
    elif x%5 == 0:
        print("Buzz")
    else:
        print(x)


    