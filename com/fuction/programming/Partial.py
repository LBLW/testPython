import functools


def partial_demo():
    # functools.partial就是帮助我们创建一个偏函数的，
    # 通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。
    # 不需要我们自己定义int2()
    # 把一个函数的某些参数给固定住（也就是设置默认值），
    # 返回一个新的函数，调用这个新函数会更简单
    # 可以在函数调用时传入其他值
    # 创建偏函数时，实际上可以接收函数对象、*args 和 **kw 这3个参数
    int2 = functools.partial(int, base=2)
    print(int2('101011'))
    print(int2('10', base=10))


partial_demo()
