# 将函数声明在一个单独的 python 文件中
# 之后再其他 python 文件中引用


def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


def my_square(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def enroll(x, a='test', b='best', c=[], d=None):
    c.append('END')
    if d is None:
        d = []
    d.append("BEGIN")
    print(x, a, b, c, d)


def calc(*numbers):
    temp_sum = 0
    for n in numbers:
        temp_sum = temp_sum + n * n

    return temp_sum


def person(name, age, **kw):
    if 'city' in kw:
        pass
    elif 'job' in kw:
        pass

    print('name:', name, 'age:', age, 'other:', kw)


def congressman(name, age, *, city, country):
    print('name:', name, 'age:', age, 'city:', city, 'country:', country)


def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)
