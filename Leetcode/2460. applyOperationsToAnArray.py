class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            else:
                continue
        zeros = nums.count(0)
        nums = [i for i in nums if i != 0]
        nums.extend([0] * zeros)
        return nums