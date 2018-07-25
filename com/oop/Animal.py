# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，
# 子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。


class Animal(object):

    def run(self):
        print('Animal running...')


class Dog(Animal):

    def run(self):
        print('Dog running...')


class Cat(Animal):

    def run(self):
        print('Cat running...')


class Duck(object):

    def run(self):
        print('duck runnig...')


def invoke():

    cat = Cat()
    cat.run()

    def auto_invoke(animal):
        animal.run()

    print(isinstance(cat, Animal))
    # 对于静态语言（例如Java）来说，如果需要传入Animal类型，
    # 则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
    # 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
    # 我们只需要保证传入的对象有一个run()方法就可以了：
    auto_invoke(Duck())


invoke()
