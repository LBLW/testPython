import types


class Info(object):
    # 如可以直接在class中定义属性，
    # 这种属性是类属性，归Student类所有
    # 实例属性和类属性使用相同的名字
    # 相同名称的实例属性将屏蔽掉类属性
    infoName = 'TypesInfo'

    def __init__(self, message):
        self.__message = message

    def get_message(self):
        return self.__message


def invoke_type():

    # 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，
    # 拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。

    def inner_method(a):
        print(type(a))
    inner_method('fuck')
    inner = Info('message')
    # 判断对象类型，使用type()函数
    # 返回对应的Class类型
    print(type(inner_method))
    print(not isinstance(inner, Info))
    print(type(Info))
    print(type(123))
    print(type(None))
    print(type('fuck') == str)
    i = Info('fuck you ')
    print(type(i))
    # 我们要判断class的类型，可以使用isinstance()函数
    print(isinstance(type(lambda x: x), types.LambdaType))
    # 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
    print(dir(i))
    print(hasattr(i, '_Info__message'))


invoke_type()
