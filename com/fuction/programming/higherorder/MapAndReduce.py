from functools import reduce


def square(a):
    return a * a


def add(a, b):
    return a + b


def map_demo():
    # map() 函数接收两个参数，一个是函数，一个是Iterable，
    # map 将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
    # map() 作为高阶函数，事实上它把运算规则抽象了
    i = map(square, range(1, 10))
    print(list(i))


def reduce_demo():
    # reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
    # reduce把结果继续和序列的下一个元素做累积计算
    print(reduce(add, range(1, 101)))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def map_reduce_demo():

    def fn(x, y):
        return x * 10 + y

    def char2num(x):
        return DIGITS[x]

    print(reduce(fn, map(char2num, '14256')))


map_reduce_demo()
