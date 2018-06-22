# 循环


def for_in_demo():
    # foreach()
    # Python的循环有两种，一种是for...in循环，
    # 依次把list或tuple中的每个元素迭代出来

    names = ['Michael', 'Bob', 'Tracy']

    for name in names:
        print(name)


def while_demo():
    # while
    # break
    # continue

    n = 1
    while n <= 100:
        if n > 10:
            break

        n = n + 1

        if n == 9:
            continue
        print(n)
    print('END')


while_demo()
