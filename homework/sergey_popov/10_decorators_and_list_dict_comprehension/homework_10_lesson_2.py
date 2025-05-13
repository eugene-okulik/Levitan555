
def repeat_me(func):

    def wrapper(args, count):
        x = 0
        while x < count:  # До этого допер сам. Через range(count) сразу не догадался, поэтому оставлю так
            func(args)
            x += 1

    return wrapper


@repeat_me
def example(text):
    print(text)


example('hello', count=2)
