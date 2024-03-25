class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return False
        rows = len(matrix)
        columns = len(matrix[0])
        for m in range(rows):
            for n in range(columns):
                if m + 1 < rows and n + 1 < columns:
                    if matrix[m][n] != matrix[m + 1][n + 1]:
                        return False
        return True