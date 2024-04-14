class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k])
        maxAverage = windowSum / k
        for i in range(k,len(nums)):
            windowSum +=nums[i]
            windowSum -= nums[i-k]
            maxAverage = max(maxAverage, windowSum/k)
        return maxAverage
        