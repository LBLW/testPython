# 在Python中，定义一个函数要使用 'def' 语句，
# 依次写出函数名、括号、括号中的参数和冒号 ':'，
# 然后，在缩进块中编写函数体，
# 函数的返回值用return语句返回。

# 文件的引用于内部函数的引用
from com.fuction.base.TempFunction import my_abs


def declare_demo():

    x = input('please input the num:')
    print(my_abs(int(x)))

    y, z = return_demo()
    print(y, z)

    b = return_demo()
    print(b)


def pass_demo():
    # 如果想定义一个什么事也不做的空函数，可以用pass
    # 就可以先放一个pass，让代码能运行起来
    pass


def return_demo():
    # 除去正常的返回值之外
    # 还支持返回多个参数
    # 实际上是返回一个 tuple

    return 1, 3


declare_demo()
