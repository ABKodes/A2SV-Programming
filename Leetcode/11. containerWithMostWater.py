class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        finalArea = 0
        while left < right:
            if height[left] < height[right]:
                tempArea = height[left] * (right - left)
                left +=1
            else:
                tempArea = height[right] * (right - left)
                right -=1
            finalArea = max(finalArea,tempArea)
        return finalArea