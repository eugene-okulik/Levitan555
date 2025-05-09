temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]


def high_fun(y):
    return filter(lambda x: x > y, temperatures)


print(min(high_fun(28)))
print(max(high_fun(28)))
print(sum(high_fun(28)) / len(list(high_fun(28))))
