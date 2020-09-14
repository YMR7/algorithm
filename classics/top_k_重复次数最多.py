# 从一百万个数中找出重复次数最多的10个数


def top_k(nums, k):
    data_dict = {}
    for num in nums:
        data_dict[num] = data_dict.get(num, 0) + 1
    i = 0
    print(data_dict)
    # 最小堆列表，存放的是字典中的key
    data_key = []
    for key in data_dict:
        # 构建最小堆
        if i == k:
            data_key = heap_sort(data_key, data_dict, k)
        # 前k个数据直接放在列表
        if i < k:
            data_key.append(key)
            i += 1
        # 第k个数据开始，每个值都与data_key[0]对比，大的话替换data_key[0]，再次构建最小堆
        else:
            if data_dict[key] > data_dict[data_key[0]]:
                data_key[0] = key
                data_key = heap_sort(data_key, data_dict, k)
    return data_key


def min_heap(data_key, data_dict, start, end):
    dad = start
    son = 2 * dad + 1
    while son <= end:
        # 有右孩子，并且右孩子比左孩子小
        if son + 1 <= end and data_dict[data_key[son + 1]] < data_dict[data_key[son]]:
            son = son + 1
        # 子节点比父节点小
        if data_dict[data_key[son]] < data_dict[data_key[dad]]:
            data_key[dad], data_key[son] = data_key[son], data_key[dad]
            dad = son
            son = 2 * dad + 1
        else:
            return


# 构建最小堆
def heap_sort(data_key, data_dict, k):
    # 最后一个父节点
    last_parent = len(data_key) // 2 - 1
    for i in range(last_parent, -1, -1):
        min_heap(data_key, data_dict, i, k - 1)
    return data_key


if __name__ == '__main__':
    arr = [1, 5, 7, 1, 2, 2, 2, 4, 5, 6, 1, 2, 10]
    print(top_k(arr, 3))
