# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，
# 然后，用raise语句抛出一个错误的实例

import logging


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value : %s' % s)
    return 10 / n


def bar():

    try:
        foo('0')
    except FooError as e:
        logging.exception(e)
        # raise语句如果不带参数，就会把当前错误原样抛出。
        raise


bar()
