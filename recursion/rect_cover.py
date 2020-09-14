# -*- coding: utf-8 -*-


def rectCover(number):
    # write code here
    # f(n) = f(n-1)(fn-2)
    if number <= 0:
        return 0
    if number == 1:
        return 1
    li = [1, 2]
    if number > 2:
        while number > 2:
            number -= 1
            li.append(li[-1] + li[-2])
    # number的值已经改变，li[number-1]不是最后一个数
    # return li[number - 1]
    return li[-1]
