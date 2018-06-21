# python 中的 list 和 tuple 结构 本质就是个数组


def list_demo():
    # Python内置的一种数据类型是列表：list。
    # list是一种有序的集合，可以随时添加和删除其中的元素。

    class_names = ['Michael', 'Bob', 'Tracy']
    print(class_names)

    # 变量classmates就是一个list。
    # 用len()函数可以获得list元素的个数

    name_number = len(class_names)
    print(name_number)

    # 用索引来访问list中每一个位置的元素，索引是从0开始的。

    print(class_names[0])
    print(class_names[1])
    print(class_names[2])
    print(class_names[-1])

    # 现阶段数组越界
    # print(classNames[3])

    # list是一个可变的有序表
    # 可以往list中追加元素到末尾：

    class_names.append('Genius')
    print(class_names)

    # 也可以把元素插入到指定的位置，
    # 比如索引号为1的位置

    class_names.insert(1, 'Abortion')
    print(class_names)

    # 移除list末尾的元素
    # 要删除指定位置的元素，用pop(i)方法，其中i是索引位置

    class_name = class_names.pop()
    print(class_name)
    print(class_names)

    class_name = class_names.pop(1)
    print(class_name)

    # list里面的元素的数据类型也可以不同

    list_name = ['Apple', 123, True]
    print(list_name)

    # 同样，也可以包含list
    temp_l = [135, 'AAA', False]
    list_name.append(temp_l)
    print(list_name)
    list_length = len(list_name)
    print(list_length)

    # 如果一个list中一个元素也没有，
    # 就是一个空的list，它的长度为0

    list_l = []
    print(list_l)
    print(len(list_l))


def tuple_demo():
    # 另一种有序列表叫元组:tuple。
    # tuple 和 list 非常类似,但是 tuple 一旦初始化就不能修改
    # 当你定义一个 tuple 时,在定义的时候, tuple 的元素就必须被确定下来

    class_names = ('Michael', 'Bob', 'Tracy')
    print(class_names)

    # 它没有append()，insert()这样的方法,
    # 其他获取元素的方法和list是一样的

    print(class_names[-1])
    print(class_names[0])

    # 空的元祖 tuple

    none_tuple = ()
    print(none_tuple)

    # 要定义一个只有1个元素的tuple,
    # tuple定义时必须加一个逗号,

    one_element_tuple = (1,)
    print(one_element_tuple)

    # tuple 中可以包含 list

    inner_list = [131, 145]
    wrap_tuple = (1, 2, 3, inner_list)

    print(wrap_tuple)

    # tuple 中的 list 元素可以被改变

    inner_list[0] = 'A'
    inner_list[1] = 'B'

    print(wrap_tuple)
    pass


# tuple_demo()
