class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hashMap = {}
         for n in nums:
            if n not in hashMap:
                hashMap[n] = 0
            else:
                return True
         return False

# Time Complexity of O(n): Going through all the "nums" list
# Space Complexity of O(n): Inserting all the elements into "nums" list