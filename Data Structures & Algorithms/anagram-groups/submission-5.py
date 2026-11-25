class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for str_value in strs:
            hash_map[str(sorted(str_value))] = hash_map.get(str(sorted(str_value)), []) + [str_value]
        print(hash_map)
        return list(hash_map.values())


        