class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = (len(matrix) * len(matrix[0])) - 1
        middle = (start + end) // 2
        while (start <= end):
            middleValue = matrix[middle // len(matrix[0])][middle % len(matrix[0])]
            if (middleValue < target):
                start = middle + 1
            elif (middleValue > target):
                end = middle - 1
            else:
                return True
            middle = (start + end) // 2
        return False