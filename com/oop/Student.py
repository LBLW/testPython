# 在Python中，定义类是通过class关键字：
class Student(object):
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
    # 特殊方法“__init__”前后分别有两个下划线！！！
    # 在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
    def __init__(self, name, age):
        # 在Python中，变量名类似__xxx__的，也就是以双下划线开头，
        # 并且以双下划线结尾的，是特殊变量，
        # 特殊变量是可以直接访问的，
        # 不是private变量，所以，不能用__name__、__score__这样的变量名
        # 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
        # 所以，仍然可以通过_Student__name来访问__name变量
        self.__name = name
        self.__age = age

    def print_student(self):
        print('%s: %s' % self.name, self.age)

    # getter setter 方法
    def get_age(self):
        if self.age < 13:
            return 'junior'
        elif self.age >= 13 & self <= 19:
            return 'teenager'
        else:
            return 'young'

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
# 和静态语言不同，Python允许对实例变量绑定任何数据，
# 也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
