class Solution:
    def isPalindrome(self, s: str) -> bool:

        j = 0
        newS = re.sub(r'[^a-zA-Z0-9]', '', s)
        for i in range(len(newS) - 1, -1, -1):
            if newS[i].lower() != newS[j].lower():
                return False
            j+=1
        return True
        