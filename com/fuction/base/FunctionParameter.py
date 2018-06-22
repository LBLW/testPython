# Python的函数定义非常简单，但灵活度却非常大。
# 除了正常定义的必选参数外，
# 还可以使用默认参数、
# 可变参数和关键字参数，
# 使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数
# 这5种参数都可以组合使用。但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

from com.fuction.base.TempFunction import *


def default_parameter_demo():
    # 位置参数
    # 声明函数时定义的入参就是位置参数
    a = my_square(10, 3)
    print(a)

    # 默认参数
    # 声明函数时定义入参的默认值，
    # 若在函数调用时未传入参数，则参数为定义时的默认值
    # 当函数有多个参数时，
    # 把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
    b = my_square(12)
    print(b)
    # 有多个默认参数时，调用的时候，既可以按顺序提供默认参数
    enroll(0, 'd', 'e')
    # 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
    enroll(0, b='c')
    # Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
    # 因为默认参数L也是一个变量，它指向对象[]，
    # 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
    # 定义默认参数要牢记一点：默认参数必须指向不变对象！
    enroll(0)


def variable_parameter_demo():

    # 可变参数
    # 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
    # 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
    # 在函数内部，参数接收到的是一个tuple
    # 调用该函数时，可以传入任意个参数，包括0个参数
    print(calc(1, 3))
    print(calc())

    # 所以Python允许你在list或tuple前面加一个*号，
    # 把list或tuple的元素变成可变参数传进去
    # *nums表示把nums这个list的所有元素作为可变参数传进去
    nums = [1, 2, 3]
    print(calc(*nums))

    # 关键字参数
    # 关键字参数允许你传入0个或任意个含参数名的参数，
    # 这些关键字参数在函数内部自动组装为一个dict。
    person('Michael', 40)
    person('Adam', 3, city='北京')
    extra = {'city': 'Shanghai', 'job': 'Whore', 'favorite': 'big black dick'}
    person('Jini', 25, **extra)

    # 如果要限制关键字参数的名字，就可以用命名关键字参数
    # 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    congressman('Marker', 47, country='American', city='California')


def recursion_demo():
    # 递归示例
    print(fact(10))


recursion_demo()
