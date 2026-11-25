class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, number in enumerate(nums):
            value = target - number
            if value in seen:
                return [seen[value], index]
            else:
                 seen[number] = index
        