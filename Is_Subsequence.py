class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lt=len(t)
        ls=len(s)
        j=0
        for i in s:
            while j<lt:
                if t[j]==i:
                    j=j+1
                    ls=ls-1
                    break
                j+=1
            if j==lt:
                    break
        if ls==0:
            return True
        return False