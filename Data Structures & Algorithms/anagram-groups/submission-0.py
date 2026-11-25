class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashStr = {}
        answer = []
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str not in hashStr:
                hashStr[sorted_str] = [string]
            else:
                hashStr[sorted_str].append(string)
        for string in hashStr:
            answer.append(hashStr[string])

        return answer
        
        