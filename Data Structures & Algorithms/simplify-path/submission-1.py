class Solution:
    def simplifyPath(self, path: str) -> str:
        if path == "/":
            return "/"
        words = []
        res = ""
        for character in path[1:]:
            if character == "/":
                if res != "":
                    words.append(res)
                    res = ""
                else:
                    continue
            else:
                res += character
        if res != "":
            words.append(res)
        s = []
        for word in words:
            if word == ".." and s:
                s.pop()
            elif word == ".." and not s:
                continue
            else:
                if word != ".":
                    s.append(word)
        return f"/{"/".join(s)}"         