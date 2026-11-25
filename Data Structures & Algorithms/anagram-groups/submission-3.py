class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            key = sorted(s)
            key = ''.join(key)
            if key not in hashMap:
                hashMap[key] = []
                hashMap[key].append(s)
            else:
                hashMap[key].append(s)
            print(hashMap)

        value = []
        for key in hashMap:
            value.append(hashMap[key])
        
        return value
        