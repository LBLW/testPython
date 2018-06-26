# 高级特性
# 通过 collections 模块的 Iterable 类型判断当前模块是否可以被迭代
from collections import Iterable
from collections import Iterator


def slices_demo():
    # Python提供了切片（Slice）操作符
    # 类似将数组切片之后取
    # 这种经常取指定索引范围的操作
    # a[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
    a = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print(a[0:3])
    # 如果第一个索引是0，还可以省略
    print(a[:3])
    # 切片的 ':' 前后都可以变动 也可以为负值，标识从数组末尾开始获取
    print(a[-2:])
    print(a[-2:-1])

    # 切片的 '::' 之后只能更数字类型，代表数组下标，表示每几个取一个
    print(a[::2])


def iterate_demo():
    # 通过 for in 操作符来进行集合的迭代
    names = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    for name in names:
        print(name)

    # 不同与 java，python 不能迭代 key : value 映射结构(Entry)
    # 直接迭代的话列出的是结构的 key
    dict_type = {'a': 'Michael', 'b': 'Sarah', 'c': 'Bob'}
    for key in dict_type:
        print(key)

    # 也可以通过 dict.values() 映射的值来迭代
    for value in dict_type.values():
        print(value)

    # 判断当前模块是否可以被迭代
    print(isinstance(dict_type, Iterable))

    # 将 list 转换成 key-value
    for i, value in enumerate(['a', 'b', 'c']):
            print(i, value)


def list_comprehensions_demo():
    # 列表生成式即List Comprehensions，
    # 是Python内置的非常简单却强大的可以用来创建list的生成式。

    print(list(range(1, 9)))

    # 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环
    l_list = []
    for x in range(1, 9):
        l_list.append(x * x)
    print(l_list)

    # 上面代码也可以换成以下写法
    l_list = [x * x for x in range(1, 9)]
    print(l_list)

    # for 循环之后可以跟 if 条件判断语句
    l_list = [x * x for x in range(1, 9) if x % 2]
    print(l_list)

    # 还可以使用两层循环，可以生成全排列
    l_list = [m + n for m in 'ABC' for n in 'XYZ']
    print(l_list)

    # for循环其实可以同时使用两个甚至多个变量，
    # 比如dict的items()可以同时迭代key和value：
    d = {'a': 'A', 'b': 'B', 'c': 'C'}
    l_list = [k + '=' + v for k, v in d.items()]
    print(l_list)


def generator_demo():
    # 通过列表生成式创建大容量的列表，所需内存太大，
    # 如果列表元素可以按照某种算法推算出来，
    # 那我们是否可以在循环的过程中不断推算出后续的元素呢？
    # 这样就不必创建完整的 list，从而节省大量的空间。
    # 这种一边循环一边计算的机制，称为生成器：generator
    # 要创建一个 generator，有很多种方法。
    # 第一种方法很简单，只要把一个列表生成式的[]改成()

    g = (x * x for x in range(1, 10))
    print(g)
    # g 是一个 generator 可以通过 next() 打印出 g 的下一个元素
    print(next(g))

    for x in g:
        print(x)

    print(fib(8))

    # 实际上 generator 是从这一段开始执行
    for y in fib(10):
        print(y)

    for y in triangle(10):
        print(y)
    s_1, s_0 = [1], [0]

    print((s_1 + s_0)[0])


# generator 和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成 generator 的函数，在每次调用 next() 的时候执行，(外部调用next())
# 遇到 yield 语句返回，再次执行时从上次返回的 yield 语句处继续执行。
def fib(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        # 如果一个函数定义中包含 yield 关键字，那
        # 么这个函数就不再是一个普通函数，而是一个 generator

        # 首次执行到这个地方发生中断
        yield b
        # 之后接着向↓接着执行
        a, b = b, a+b
        n = n+1

        # 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
        # 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
    return 'done'


def triangle(max_length):
    a, L = 0, [1]
    while a < max_length:
        yield L
        L = [(L+[0])[i] + ([0]+L)[i] for i in range(len(L) + 1)]
        a = a + 1


def iterable_demo():
    # 而生成器不但可以作用于 for 循环，还可以被 next() 函数不断调用并返回下一个值，
    # 直到最后抛出 StopIteration 错误表示无法继续返回下一个值了。
    # 可以被 next() 函数调用并不断返回下一个值的对象称为迭代器: Iterator。
    # 可以使用 isinstance() 判断一个对象是否是 Iterator 对象

    print(isinstance((x for x in range(1, 4)), Iterator))
    print(isinstance([], Iterator))
    print(isinstance({}, Iterator))
    print(isinstance('abc', Iterator))

    # 生成器都是 Iterator 对象，但 list、dict、str 虽然是 Iterable，却不是 Iterator
    # 把 list、dict、str 等 Iterable 变成 Iterator 可以使用 iter() 函数

    print(isinstance(iter([]), Iterator))
    print(isinstance(iter('abc'), Iterator))


generator_demo()
