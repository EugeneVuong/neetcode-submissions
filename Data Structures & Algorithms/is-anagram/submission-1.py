class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMapS = {}
        for c in s:
            if c not in hashMapS:
                hashMapS[c] = 1
            else:
                hashMapS[c] = hashMapS[c] + 1
        
        hashMapT = {}
        for c in t:
            if c not in hashMapT:
                hashMapT[c] = 1
            else:
                hashMapT[c] = hashMapT[c] + 1
        
        return hashMapT == hashMapS



        