class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxWidth = 0
        numberOfZeros = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                numberOfZeros +=1
            # If the number of zeros exceeds k, move the left pointer to the right side
            while numberOfZeros > k:
                if nums[left] == 0:
                    numberOfZeros -=1
                left +=1
            maxWidth = max(maxWidth, right - left + 1)
        return maxWidth