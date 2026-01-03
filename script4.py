while True:
    print ("Hello this is a calculator ")
    m = float(input("Enter number: "))
    n = float(input("Enter number 2: "))

    q = input("+,-,/,*?")
    if q == "+":
        result = m + n
        print(result)
    elif q == "-":
        result = m - n
        print(result)
    elif q == "*":
        result = m * n
        print(result)
    elif  q == "/":
        if m == 0:
            if n == 0:
                print ("you can't divide zero by zero")
                break
    elif q == "/":
        result = m / n
        print(result)
    for i in range(5):
        if input ("would you like to continue the equation").lower().startswith("y"):
            x = float (input("number?"))
            q = input ("+,-,/,*?")
            if q == "+":
                newresult = (result) + x
                print(newresult)
            elif q == "-":
                newresult = m - x
                print(newresult)
            elif q == "*":
                newresult = (result) * x
                print(newresult)
            elif q == "/":
                if (result) == 0:
                    if x == 0:
                        print("you can't divide zero by zero")
                        break
            elif q == "/":
                newresult = (result) / x
                print(newresult)
            (result)= (newresult)
        else :
            break
exit()