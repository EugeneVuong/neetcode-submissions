'''
We can determine if it is a Valid Anagram if the length are the same.
Additionally, we can use a hash_map to keep track of each character in the string (regarding the amount)

n = the length of the string for both s and t
We can determine this is o(n) space complexity since we storing it in the hashmap
We can determine this is o(n) time complexity since we are tranversing the strings
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map_s = {}
        hash_map_t = {}
        
        for i in range(len(s)):
            hash_map_s[s[i]] = hash_map_s.get(s[i], 0) + 1
            hash_map_t[t[i]] = hash_map_t.get(t[i], 0) + 1
        
        return hash_map_s == hash_map_t
