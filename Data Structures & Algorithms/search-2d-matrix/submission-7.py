class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startRow = 0
        endRow = len(matrix) - 1
        rowReturned = 0
        while (startRow <= endRow):
            middleRow = (startRow + endRow) // 2

            if (target < matrix[middleRow][0]):
                endRow = middleRow - 1


            elif (target > matrix[middleRow][-1]):
                startRow = middleRow + 1

            else:
                rowReturned = middleRow
                break
        left = 0
        right = len(matrix[rowReturned]) - 1
        print(matrix[rowReturned])

        while (left <= right):
            middle = (left + right) // 2
            if (matrix[rowReturned][middle] < target):
                left = middle + 1
            elif (matrix[rowReturned][middle] > target):
                right = middle - 1
            else:
                return True

        return False



