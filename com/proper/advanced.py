# 高级特性
# 通过 collections 模块的 Iterable 类型判断当前模块是否可以被迭代
from collections import Iterable


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


list_comprehensions_demo()
