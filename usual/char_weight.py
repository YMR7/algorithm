'''
有 n 个字符串，每个字符串都是由 A-J 的大写字符构成。
现在你将每个字符映射为一个 0-9 的数字，不同字符映射为
不同的数字。这样每个字符串就可以看做一个整数，唯一的要
求是这些整数必须是正整数且它们的字符串不能有前导零。现
在问你怎样映射字符才能使得这些字符串表示的整数之和最大？
'''

# 1. 计算字母的权重，个位为1，十位为10，百位为100，以此类推
# 2.对权重进行排序，最大的指向9，次大指向8，类推，未出现的字母指向0
# 3.首字母不能为0，出现字母数为10时，判断首字母是否为0
# 3.1 为0,依序寻找第一个首字母不为0的字母,删除,让字母数量变为9
# 4.权重与指向的数字相乘


def get_max(strs, n):
    str_map = {}
    
    first_set = set()
    for i in range(n):
        length = len(strs[i])
        count = 1
        # 首字母集合
        first_set.add(strs[i][0])
        for j in range(length-1, -1, -1):
            c = strs[i][j]
            if c in str_map:
                str_map[c] += count
            else:
                str_map[c] = count
            count *= 10
    sorted_list = sorted(str_map.items(), key=lambda x: x[1], reverse=True)

    # 首字母不能为0
    if len(sorted_list) == 10:
        for i in range(9, -1, -1):
            # key=0
            key = sorted_list[i][0]
            if key not in first_set:
                del sorted_list[i]
                break
    res = 0
    i = 0
    k = 9
    while i < len(sorted_list):
        res += sorted_list[i][1] * k
        i += 1
        k -= 1
    print(res)
    return res


if __name__ == '__main__':
    n = int(input())
    input_str = []
    for i in range(n):
        s = input()
        input_str.append(s)
    get_max(input_str, n)
