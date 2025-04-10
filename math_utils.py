def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero"

def power(x, y):
    return x ** y

def mod(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return "Error: Division by zero"

# Test cases
if __name__ == "__main__":
    print("Test cases:")
    print(f"add(5, 8) = {add(5, 8)}")
    print(f"subtract(7, 9) = {subtract(7, 9)}")
    print(f"multiply(6, 8) = {multiply(6, 8)}")
    print(f"divide(4, 0) = {divide(4, 0)}")
    print(f"power(5, 2) = {power(5, 2)}")
    print(f"mod(5, 2)= {mod(5,2)}")
