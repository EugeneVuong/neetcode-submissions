class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for str_value in strs:
           encode_str += "#" + str(len(str_value)) + "#" + str_value
        print(encode_str)
        return encode_str

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                i += 1
                count = ""
                while s[i] != "#":
                    count += s[i]
                    i += 1
                count = int(count)
                i += 1
                j = 0
                string = ""
                while j < count:
                    string += s[i]
                    i += 1
                    j += 1
                decoded.append(string)
        return decoded



