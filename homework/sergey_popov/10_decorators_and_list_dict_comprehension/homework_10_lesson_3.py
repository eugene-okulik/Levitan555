a = int(input())
b = int(input())


def oper(func):
    def wrapper(*args):
        num1, num2 = args
        if num1 == num2:
            operation = '+'
            result = func(a, b, operation)
            return result

        elif num1 < 0 or num2 < 0:
            operation = '*'
            result = func(a, b, operation)
            return result

        elif num1 > num2:
            operation = '-'
            result = func(a, b, operation)
            return result

        else:
            operation = '/'
            result = func(a, b, operation)
            return result

    return wrapper


@oper
def calc(first, second, operation):
    if operation == '+':
        operation = first + second
    elif operation == '-':
        operation = first - second
    elif operation == '/':
        operation = first / second
    elif operation == '*':
        operation = first * second
    return operation


print(calc(a, b))
