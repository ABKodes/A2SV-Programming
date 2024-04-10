class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        size = len(arr)
        for index in range(size):
            # Setting the maximum value and the index of that value
            maxValue = max(arr[:size-index])
            maxIndex = arr.index(maxValue) + 1
            # Bringing the max value to the zero index
            arr[:maxIndex] = reversed(arr[:maxIndex])
            result.append(maxIndex)
            # Taking the value to the designated index
            arr[:size-index] = reversed(arr[:size-index])
            result.append(size-index)
        return result
