class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        lens = []
        for s in strs:
            lens.append(len(s))

        res = ""
        for l in lens:
            res += f"{l},"

        res += "$"

        for s in strs:
            res += f"{s}"
        
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sizes = []
        res = []
        i = 0

        while s[i] != "$":
            curr = ""
            while s[i] != ",":
                curr += s[i]
                i += 1
            sizes.append(int(curr))
            i += 1
        i += 1
        for size in sizes:
            res.append(s[i:i+size])
            i += size
        return res