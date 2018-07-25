from types import MethodType


class Student(object):
    # Python允许在定义class的时候，
    # 定义一个特殊的__slots__变量，
    # 来限制该class实例能添加的属性
    __slots__ = ('name', 'age')

    # toString method
    def __str__(self):
        return 'Student object(name: %s)' % self.name


class JuniorStudent(Student):

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self.age = age


def set_age(self, age):
    self.age = age


def set_scope(self, scope):
    self.scope = scope


def dynamic_demo():
    # 动态绑定属性
    a = Student()
    a.name = 'Alice'
    print(a.name)

    # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    JuniorStudent.set_scope = MethodType(set_scope, JuniorStudent)

    d = JuniorStudent()
    d.set_scope(99)
    print(d.scope)

    # 动态绑定方法
    a.set_age = MethodType(set_age, a)
    a.set_age(26)
    print(a.age)

    # 给一个实例绑定的方法 对另一个实例是不起作用的
    # b = Student()
    # b.set_age(36)
    # print(b.age)

    # 可以给class绑定方法 所有实例均可调用
    # 由于'score'没有被放到__slots__中，
    # 所以不能绑定score属性
    Student.set_scope = MethodType(set_scope, Student)

    c = Student()
    c.set_scope(99)
    print(c.scope)


# 定制类
class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            return StopIteration()
        return self.a

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a

    def __getattr__(self, item):
        return item

    def __call__(self, *args, **kwargs):
        return None


def method_demo():
    student = Student()
    student.name = 'Alice'
    print(student)

    for f in Fib():
        print(f)


method_demo()
