
def fibo(param):
    n = 1.618
    num = 1
    count = 1
    while count < param:
        yield num
        num *= n
        count += 1


def fibo_num(num):
    count = 1
    for number in fibo(100001):
        if count == num:
            return number
        count += 1


print(fibo_num(5))
print(fibo_num(200))
print(fibo_num(1000))
print(fibo_num(100000))
