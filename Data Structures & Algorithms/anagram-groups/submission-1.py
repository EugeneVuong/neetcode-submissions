class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     hashStr = {}
    #     answer = []
    #     for string in strs:
    #         sorted_str = ''.join(sorted(string)) # Sorted is n log (n)
    #         if sorted_str not in hashStr:
    #             hashStr[sorted_str] = [string]
    #         else:
    #             hashStr[sorted_str].append(string)
    #     for string in hashStr:
    #         answer.append(hashStr[string])

    #     return answer

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for string in strs:
            chars = [0] * 26
            for char in string:
                chars[ord(char) - ord('a')] = chars[ord(char) - ord('a')] + 1
            if tuple(chars) not in hashMap:
                hashMap[tuple(chars)] = [string]
            else:
                hashMap[tuple(chars)].append(string)
        return hashMap.values()
    
        