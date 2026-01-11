def calculator():
    x = float(input("Enter number: "))
    y = float(input("Enter number 2: "))
    operator = input("+,-,/,*?")

    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    elif operator == "*":
        print(x * y)
    elif operator == "/":
        print(x / y)