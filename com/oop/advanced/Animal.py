class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:
class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。
# 这种设计通常称之为MixIn。
class Runnable(object):

    def run(self):
        print('Running...')


class Flyable(object):

    def fly(self):
        print('Flying...')


# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass
