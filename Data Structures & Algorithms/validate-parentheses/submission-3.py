class Solution:
    def isValid(self, s: str) -> bool:
        newS = []

        for c in s:
            if len(newS) > 0:
                ord1 = ord(newS[-1])
                ord2 = ord(c)

                diff = abs(ord1 - ord2)
                
                if diff > 0 and diff <= 2 and ord2 > ord1:
                    newS.pop()
                else:
                    newS.append(c)
            else:
                newS.append(c)
                
        return len(newS) == 0

        

        