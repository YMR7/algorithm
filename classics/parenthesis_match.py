# aaa()aaa、afka(sf)hio{f}:输出‘true’
# fbajk(fa{df}):输出‘false’


def test(strs):
    dict_map = {'(': ')', '{': '}', '[': ']'}
    temp = ['(', '[', '{', ')', ']', '}']
    li = []
    for char in strs:
        if char in temp:
            li.append(char)
        length = len(li)
        # 长度为二时可以组成一个括号，li[0]必须是左括号，li[1]必须是li[0]对应的右括号
        if length == 2:
            if li[0] in dict_map and dict_map[li[0]] == li[1]:
                li = []
            else:
                return 'false'
    return 'true'


if __name__ == '__main__':
    print(test('fbajk(fa{df})'))
