class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        counter = 0
        nums.sort()
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                counter += 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return counter
