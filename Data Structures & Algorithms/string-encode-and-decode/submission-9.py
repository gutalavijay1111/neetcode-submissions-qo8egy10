class Solution:

    # will create a string "5#abcde4#wwdw"
    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += f"{len(word)}#{word}"
            print("encoded >> ", result)
        return result

    def decode(self, s: str) -> List[str]:

        i = 0
        result = []
        while i < len(s):
            word = ""
            word_len = ""

            while s[i] != "#":
                word_len += s[i]
                i += 1
                
            word_len = int(word_len)
            i += 1 #skipping hash 

            word = s[i:i+word_len]
            print(">> word", word)
            result.append(word)
            i += word_len

        return result


