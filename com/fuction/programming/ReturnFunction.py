# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回


def return_demo(*args):
    # 闭包内部函数可以引用外部函数的参数和局部变量，
    # 当外部函数返回函数内部函数时，
    # 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）

    ## 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
    def return_fun():
        print(args)
        for arg in args:
            print('in return function ' + arg)
    return return_fun


def invoke():
    r_f = return_demo('a', 'b', 'c', 'd')
    print(r_f)
    print(r_f())


def closure_demo():

    def old_count():
        fs = []
        for i in range(1, 4):
            def f():
                return i * i
            fs.append(f)
        return fs
    f1, f2, f3 = old_count()
    print(f1(), f2(), f3())

    def new_count():
        def f(j):
            return lambda: j*j
        fs = []
        for i in range(1, 4):
            fs.append(f(i))
        return fs
    f4, f5, f6 = new_count()
    print(f4(), f5(), f6())


closure_demo()

