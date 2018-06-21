# python 中的 list 和 tuple 结构 本质就是个数组


def list_demo():
    # Python内置的一种数据类型是列表：list。
    # list是一种有序的集合，可以随时添加和删除其中的元素。

    classNames = ['Michael', 'Bob', 'Tracy']
    print(classNames)

    # 变量classmates就是一个list。
    # 用len()函数可以获得list元素的个数

    nameNumber = len(classNames)
    print(nameNumber)

    # 用索引来访问list中每一个位置的元素，索引是从0开始的。

    print(classNames[0])
    print(classNames[1])
    print(classNames[2])
    print(classNames[-1])

    # 现阶段数组越界
    # print(classNames[3])

    # list是一个可变的有序表
    # 可以往list中追加元素到末尾：

    classNames.append('Genius')
    print(classNames)

    # 也可以把元素插入到指定的位置，
    # 比如索引号为1的位置

    classNames.insert(1, 'Abortion')
    print(classNames)

    # 移除list末尾的元素
    # 要删除指定位置的元素，用pop(i)方法，其中i是索引位置

    className = classNames.pop()
    print(className)
    print(classNames)

    className = classNames.pop(1)
    print(className)

    # list里面的元素的数据类型也可以不同

    listName = ['Apple', 123, True]
    print(listName)

    # 同样，也可以包含list
    tempL = [135, 'AAA', False]
    listName.append(tempL)
    print(listName)
    listLength = len(listName)
    print(listLength)

    # 如果一个list中一个元素也没有，
    # 就是一个空的list，它的长度为0

    listL = []
    print(listL)
    print(len(listL))


def tuple_demo():
    # 另一种有序列表叫元组:tuple。
    # tuple 和 list 非常类似,但是 tuple 一旦初始化就不能修改
    # 当你定义一个 tuple 时,在定义的时候, tuple 的元素就必须被确定下来

    classNames = ('Michael', 'Bob', 'Tracy')
    print(classNames)

    # 它没有append()，insert()这样的方法,
    # 其他获取元素的方法和list是一样的

    print(classNames[-1])
    print(classNames[0])

    # 空的元祖 tuple

    noneTuple = ()
    print(noneTuple)

    # 要定义一个只有1个元素的tuple,
    # tuple定义时必须加一个逗号,

    oneElementTuple = (1,)
    print(oneElementTuple)

    # tuple 中可以包含 list

    innerList = [131, 145]
    wrapTuple = (1, 2, 3, innerList)

    print(wrapTuple)

    # tuple 中的 list 元素可以被改变

    innerList[0] = 'A'
    innerList[1] = 'B'

    print(wrapTuple)
    pass


# tuple_demo()
