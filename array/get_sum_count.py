# 给定四个包含整数的数组列表 A , B , C , D ,
# 计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，
# 且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。


# 1.计算AB的和，存到{}中
# 2.计算CD的和，判断其相反数是否在{}中
def get_num(nums, n):
    ab_map = {}
    count = 0
    for a in nums[0]:
        for b in nums[1]:
            ab_map[a+b] = ab_map.get(a+b, 0) + 1
    for c in nums[2]:
        for d in nums[3]:
            temp = c + d
            if -temp in ab_map:
                # 相反数不一定只有一个
                count += ab_map[-temp]
    return count


if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(4):
        li = []
        for j in range(n):
            li.append(int(input()))
        nums.append(li)
    res = get_num(nums, n)
    # print(len(res))
    print(res)
