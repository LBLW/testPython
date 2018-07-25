class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s' % name)


def hel(self, name='world'):
    print('Hello, %s' % name)


def hello_demo():
    h = Hello()
    h.hello()
    # 类的类型是 type
    # 实例的类型是 class
    print(type(Hello))
    print(type(h))

    # 使用 type 动态的创建一个类
    Hel = type('Hello', (object,), dict(hel=hel))

    hh = Hel()
    hh.hel()

    # 通过type()函数创建的类和直接写class是完全一样的，
    # 因为Python解释器遇到class定义时，
    # 仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。


hello_demo()
