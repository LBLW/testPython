#!/usr/bin python
# _*_ coding: utf-8 _*_

repr('a test module')
__author__ = 'Mr wang'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print("hello, world")
    elif len(args) == 2:
        print("Hello, %s !" % args[1])
    else:
        print("Too many argument! ")


if __name__ == '__main__':
    test()

# 第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
# 第2行注释表示.py文件本身使用标准UTF-8编码；
# 第4行是一个字符串` a test module `（python 3.6 不支持），
# 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
# 第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
#
# 以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。
# 后面开始就是真正的代码部分。
#
# 你可能注意到了，使用sys模块的第一步，就是导入该模块
# 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。
# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
#   运行python3 hello.py获得的sys.argv就是['hello.py']；
#   运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。
#
# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。


# 作用域
# 在一个模块中，我们可能会定义很多函数和变量，
# 但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。
# 在Python中，是通过 '_' 前缀来实现的。
# 通过pip命令来安装第三方包。

def _private_demo():
    pass

