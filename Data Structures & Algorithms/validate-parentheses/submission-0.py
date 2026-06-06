class Solution:
    def isValid(self, s: str) -> bool:
        s1 =[]
        closeToOpen = {')':'(','}':'{',']':'['}
        for i in s:
            if i in closeToOpen:
                if s1 and s1[-1]==closeToOpen[i]:
                    s1.pop()
                else:
                    return False
            else:
                s1.append(i)
        if not s1:
            return True
        else:
            return False

