# 条件判断


def judge_demo():
    # 根据Python的缩进规则，
    # 如果if语句判断是True，
    # 就把缩进的 两行 print语句执行了
    # else 相同执行行数
    # 条件中可以增加变量
    # 非零数值、非空字符串、非空list等，就判断为True，否则为False。

    age = 13
    if age >= 18:
        print('your age is ', age)
        print('adult')
    # elif => else if() 的意思
    elif age >= 6:
        print('your age is ', age)
        print('teenager')
    else:
        print('your age is', age)
        print('kid')


def data_exchange():
    # 数据转型

    input_data = input('please input some number : ')
    input_number = int(input_data)
    print(input_number)


# judge_demo()
