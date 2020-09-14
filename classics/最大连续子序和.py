# 最大连续子序列和

"""
判断前 n 个数字之和是否大于 0
"""

def test(nums):
    if not nums:
        return
    size = len(nums)
    if size == 1:
        return nums[0]
    sum = nums[0]
    tmp_sum = sum
    for i in range(1, size):
        if tmp_sum > 0:
            tmp_sum += nums[i]
        else:
            tmp_sum = nums[i]
        sum = max(tmp_sum, sum)
    return sum