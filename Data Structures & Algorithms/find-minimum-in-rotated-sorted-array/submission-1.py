class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower = 0
        upper = len(nums) - 1
        minValue = nums[0]
        while (lower <= upper):
            middle = (upper + lower) // 2
            minValue = min(minValue, nums[middle])
            if (nums[middle] < nums[upper]):
                upper = middle - 1
            else:
                lower = middle + 1



        return minValue

        