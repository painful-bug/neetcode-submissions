class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hsmp = sorted(list(s1))
        n = len(s2)
        if n < len(s1) : return False
        i, j = 0, len(s1)
        while i < n and j <= n:
            substring = sorted(list(s2[i:j]))
            if substring == hsmp:
                return True
            else:
                i+=1
                j+=1
        return False