# 装饰器
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator
# 本质上，decorator就是一个返回函数的高阶函数。


def logs(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("%s %s " % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@logs('test')
def temp():
    print("temp function ")


def decorator_demo():
    temp()


decorator_demo()
