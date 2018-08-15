# 异常处理机制
# python中内置了一套try...except...finally...
# 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，
# 它不但捕获该类型的错误，还把其子类也“一网打尽”。
# Python所有的错误都是从BaseException类派生的
# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
# 比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，
# 这时，只要main()捕获到了，就可以处理

# Python内置的logging模块可以非常容易地记录错误信息
# 通过配置，logging还可以把错误记录到日志文件里
import logging


def except_demo():

    try:
        a = 10 / 0
        print(a)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        logging.exception(e)
    else:
        print('T')
    finally:
        print('execute this')

    print('END')


except_demo()
