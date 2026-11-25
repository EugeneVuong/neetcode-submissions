class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        middle = int((start + end) // 2)
        while (start <= end):
            if (nums[middle] < target):
                start = middle + 1

            elif (nums[middle] > target):
                end = middle - 1
            else:
                return middle
            middle = int((start + end) // 2)
        return -1


        