class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for str_value in strs:
            str_list = [0] * 26
            for chr_value in str_value:
                str_list[ord(chr_value) - ord('a')] = str_list[ord(chr_value) - ord('a')] + 1
            hash_map[str(str_list)] = hash_map.get(str(str_list), []) + [str_value]
        return list(hash_map.values())




        