class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            size = len(word)
            tmp = f"{size}#{word}"
            res += tmp
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the separator after the length.
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            end = start + length

            res.append(s[start:end])

            # Jump to the next length prefix.
            i = end

        return res