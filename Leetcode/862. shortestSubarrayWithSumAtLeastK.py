class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Initialize deque with a starting point
        queue = deque([(-1, 0)])
        currentSum = 0  
        index = 0  
        shortLength = float('inf')  
        
        for num in nums:
            currentSum += num  # Update prefix sum
            
            # Remove elements from queue while the subarray sum is >= k
            while queue and currentSum - queue[0][1] >= k:
                shortLength = min(shortLength, index - queue.popleft()[0])
            
            # Maintain the monotonicity of the queue
            while queue and currentSum <= queue[-1][1]:
                queue.pop()
            
            # Add current prefix sum to the queue
            queue.append((index, currentSum))
            
            # Move to next index
            index += 1  
        
        # Return result, -1 if no valid subarray found
        return -1 if shortLength == float('inf') else shortLength
