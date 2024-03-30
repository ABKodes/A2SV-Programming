class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0,len(nums),1):
            count = 0
            for j in range(0,len(nums),1):
                if nums[i] > nums[j] and i != j:
                    count+=1
            result.append(count)
        return result
