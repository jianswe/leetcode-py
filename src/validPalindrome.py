class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                if self.validSubPalin(s, i+1, j):
                    return True 
                return self.validSubPalin(s, i, j-1)
            i+=1
            j-=1
        return True 
    
    def validSubPalin(self, s: str, start: int, end: int) -> bool: 
        i, j = start, end 
        while i<j:
            if s[i] != s[j]:
                return False 
            i+=1
            j-=1
        return True 