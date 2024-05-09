class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squareRoot = int(math.sqrt(c))
        result = []
        for i in range(squareRoot+1):
            result.append(i*i)
        left = 0
        right = len(result) - 1
        while left <= right:
            if result[left] + result[right] == c:
                return True
            elif result[left] + result[right] < c:
                left +=1
            else:
                right -=1
        return False