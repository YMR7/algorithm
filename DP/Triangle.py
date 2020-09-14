"""
1
2 9
4 8 6
4 9 5 7

"""


def get_max(nums, n):
    li = nums[n - 1]
    temp = n - 1
    count = n - 1
    for j in range(count):
        for i in range(temp):
            li[i] = max(li[i], li[i + 1]) + nums[temp-1][i]
        temp -= 1

    return li[0]


if __name__ == '__main__':
    triangle = [[1], [2, 4], [5, 9, 4]]
    res = get_max(triangle, 3)
    print(res)