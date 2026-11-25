class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += s
            encode += "\0"
        return encode

    def decode(self, s: str) -> List[str]:
        string = ""
        decode = []
        for c in s:
           if c == "\0":
            decode.append(string)
            string = ""
           else:
            string += c
        return decode
           
            