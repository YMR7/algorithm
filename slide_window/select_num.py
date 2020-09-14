"""
给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。
返回的结果必须要是按升序排好的。
如果有两个数与 x 的差值一样，优先选择数值较小的那个数。
输入描述:
第一行为排序好的数组arr
第二行为查找的个数k
第三行为基准值x
输出描述:
按升序排好的的数组
示例1输入输出示例仅供调试，后台判题数据一般不包含示例

输入
1,2,3,4,5
4
3

输出
1,2,3,4
说明
k 的值为正数，且总是小于给定排序数组的长度
数组不为空，且长度不超过 104
数组里的每个元素与 x 的绝对值不超过 104
"""


#
def test(array, k, x):
    if not array or not k or not x:
        return
    length = len(array)
    left = 0
    right = length - 1
    count = length - k
    while count:
        if x - array[left] <= array[right] - x:
            right -= 1
        else:
            left += 1
        count -= 1
    res = array[left:left + k]
    res = list(map(str, res))
    return ','.join(res)


if __name__ == '__main__':
    array = list(map(int, input().split(',')))
    k = int(input())
    x = int(input())
    print(test(array, k, x))
