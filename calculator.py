
x = float(input("Enter the first number: "))
x1 = float(input("Enter the second number: "))

while True:
    d = input("Enter the operation (+, -, *, /) or press Enter to exit: ")
    
    if d == "+":
        a = x + x1
    elif d == "*":
        a = x * x1
    elif d == "-":
        a = x - x1
    elif d == "/":
        if x1 != 0:
            a = x / x1
        else:
            print("Error: Division by zero.")
            continue
    elif d == "":
        break
    else:
        print("Invalid operation.")
        continue

    print(f"Result: {a}")
