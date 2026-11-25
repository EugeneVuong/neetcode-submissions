class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in hashSet and hashSet[j] != i:
                return [hashSet[j], i]
            hashSet[nums[i]] = i

            
