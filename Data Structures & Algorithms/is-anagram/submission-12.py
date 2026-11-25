class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for index, char in enumerate(s):
            s_dict[s[index]] = s_dict.get(s[index], 0) + 1
            t_dict[t[index]] = t_dict.get(t[index], 0) + 1
        return s_dict == t_dict
            