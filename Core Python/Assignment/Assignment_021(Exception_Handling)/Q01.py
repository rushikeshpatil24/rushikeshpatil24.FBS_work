# Basic calculator with exception handling

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    if op == '+':
        ans = a + b
    elif op == '-':
        ans = a - b
    elif op == '*':
        ans = a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError
        ans = a / b
    else:
        raise ValueError("Invalid operator")

    print("Result:", ans)

except ValueError as e:
    print("Error:", e)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
