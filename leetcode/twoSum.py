# 默认一定存在
# way one
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 返回nums升序排列的下标
        sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
        head = 0
        tail = len(nums) - 1
        sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        while sum_result != target:
            if sum_result > target:
                tail -= 1
            elif sum_result < target:
                head += 1
            sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        return [sorted_id[head], sorted_id[tail]]


# way two
class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        nums_bak = nums.copy()
        i = 0
        result = []             
        while len(nums) > 0:
            temp = nums_bak[i]  
            # 避免使用相同值，temp == pop
            nums_bak[i] = 'x'
            pop = nums.pop(0)           
            if target - pop in nums_bak:
                nub = nums_bak.index(target - pop)
                if i != nub:
                    result.append(i)
                    result.append(nub)
                    break
            nums_bak[i] = temp
            i += 1
        return result


# way 3
def twoSum(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]



