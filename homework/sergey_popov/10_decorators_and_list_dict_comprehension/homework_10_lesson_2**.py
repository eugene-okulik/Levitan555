
def repeat_me2(count):
    def decorator(func):
        def wrapper(args):
            for x in range(count):
                result = func(args)
            return result
        return wrapper
    return decorator


@repeat_me2(count=2)
def example2(text):
    print(text)


example2('print me')
