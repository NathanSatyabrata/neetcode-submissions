class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""

        for i in range(len(strs[0])):
            for s in strs:
                try:
                    if s[i] != strs[0][i]:
                        return string
                except:
                    return string
            string += strs[0][i]

        return string

        