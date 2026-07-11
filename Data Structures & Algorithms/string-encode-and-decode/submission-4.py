class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            res += f"{length}#{word}"

        return res

    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0

        while index < len(s):
            i = index

            while s[i] != "#":
                i += 1

            length = int(s[index:i])

            word_start = i + 1
            word_end = word_start + length

            decoded.append(s[word_start:word_end])

            index = word_end

        return decoded
