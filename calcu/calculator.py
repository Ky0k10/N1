def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


if __name__ == "__main__":
    a = float(input("Первое число: "))
    op = input("Операция (+ - * /): ")
    b = float(input("Второе число: "))

    ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
    if op in ops:
        print("Результат:", ops[op](a, b))
    else:
        print("Неизвестная операция")