def add(str1, str2, str_list):
    list1 = list(reversed(list(str1)))
    list2 = list(reversed(list(str2)))
    sum = 0  # 每两位相加之和
    tmp = 0  # 进位
    result = list()  #结果

    for i in range(max(len(list1), len(list2))):
        try:
            first = list1[i]
        except:
            first = '0'
        try:
            second = list2[i]
        except:
            second = '0'
        sum = str_list.index(first) + str_list.index(second) + tmp

        if sum < 36:  # 没有进位的情况
            tmp = 0
            result.append(str_list[sum])
        else:  # 有进位的情况
            tmp = sum // 36
            result.append(str_list[sum % 36])
    if tmp:
        result.append('1')
    return ''.join(list(reversed(result)))


if __name__ == '__main__':
    str_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(add('z1y1', '112z', str_list))  # a211
