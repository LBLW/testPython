# Python内置了字典 Dict 和 Set


def dict_demo():
    # dict的支持，dict全称dictionary，
    # 在其他语言中也称为map

    people = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print(people['Bob'])

    # 数据放入dict的方法

    people['Adam'] = 65
    print(people)

    # key 不存在就报错
    # print(people['Thomas'])

    # 通过in判断key是否存在
    # dict提供的get()方法，
    # 如果key不存在，可以返回None，或者自己指定的value

    print('Thomas' in people)
    print(people.get('Thomas'))
    print(people.get('Thomas', -1))

    # 要删除一个key，用pop(key)方法，对应的value也会从dict中删除

    print(people.pop('Adam'))
    print(people)

    # list比较，dict有以下几个特点:
    #   查找和插入的速度极快，不会随着key的增加而变慢；
    #   需要占用大量的内存，内存浪费多。
    # 而list相反:
    #   查找和插入的时间随着元素的增加而增加；
    #   占用空间小，浪费内存很少。


def set_demo():
    # set和dict类似，也是一组key的集合，但不存储value。
    # 由于key不能重复，所以，在set中，没有重复的key。
    # 要创建一个set，需要提供一个list作为输入集合

    number_list = [1, 2, 4, 3, 5]
    print(number_list)

    #不可以放入可变对象
    # 因为无法判断两个可变对象是否相等
    # 也就无法保证set内部“不会有重复元素”

    # number_list_2 = [4, 8, 0, 32]
    # class_names = set(number_list, number_list_2)

    class_names = set(number_list)
    print(class_names)

    # 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果

    class_names.add(7)
    class_names.add(7)
    class_names.add(7)

    print(class_names)

    # 通过remove(key)方法可以删除元素

    class_names.remove(5)
    print(class_names)
