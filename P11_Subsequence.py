class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: 
            return True
                
        j = 0 
        for char in t:
            if char == s[j]: 
                j += 1
            if j == len(s):
                return True
        
        return False 

solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc")) 
print(solution.isSubsequence("axc", "ahbgdc")) 