

def fix_demo():
    # Python内建的filter()函数用于过滤序列。

    def is_odd(n):
        return n % 2 == 1

    # 和map()类似，filter()也接收一个函数和一个序列。
    # 和map()不同的是，filter()把传入的函数依次作用于每个元素，
    # 然后根据返回值是True还是False决定保留还是丢弃该元素。
    # filter()函数返回的是一个Iterator，也就是一个惰性序列，
    # 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
    print(list(filter(is_odd, range(1, 10))))


def sort_demo():
    # sorted()也是一个高阶函数。
    # 用sorted()排序的关键在于实现一个映射函数。

    def sort_key(a):
        print(a)
        return abs(a)

    # sorted()函数就可以对list进行排序
    sort_list = [1, 12, 44, 0, -1, 44]
    print(sorted(sort_list))

    # sorted()函数也是一个高阶函数，
    # 它还可以接收一个key函数来实现自定义的排序，
    # 例如按绝对值大小排序
    print(sorted(sort_list, key=sort_key))

    sort_str_list = ['bob', 'about', 'Zoo', 'crate']
    print(sorted(sort_str_list))

    # 要进行反向排序，可以传入第三个参数reverse=True
    print(sorted(sort_list, reverse=True))


sort_demo()
