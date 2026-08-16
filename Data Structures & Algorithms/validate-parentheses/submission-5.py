class Solution:
    def isValid(self, s: str) -> bool:
        newS = []
        closeToOpen = {"}": "{", ")": "(", "]": "["}

        for c in s:
            if c in closeToOpen:
                if newS and newS[-1] == closeToOpen[c]:
                    newS.pop()
                else:
                    return False
            else:
                newS.append(c)

        return not newS

        

        