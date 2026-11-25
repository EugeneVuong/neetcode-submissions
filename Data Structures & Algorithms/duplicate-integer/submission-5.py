
"""
We want to check if there is a duplicate in nums.
That would mean we would need a hashmap.
We have to transverse through the nums array and append the values.
If the same value from nums are in the hashmap, then there is a duplicate.
"""


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if hash_map.get(num) != None:
                return True
            hash_map[num] = 1
        return False

