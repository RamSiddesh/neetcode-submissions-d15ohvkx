class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        temp = []
        for i in s:
            if i.isalnum() is False:
                continue
            else:
                temp.append(i.lower())
        if temp == temp[::-1]:
            return True
        else:
            return False