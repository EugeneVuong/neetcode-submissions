class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for count, num in enumerate(nums):
            value = target - num
            if value in hashMap:
                return [hashMap[value], count]
            hashMap[num] = count

