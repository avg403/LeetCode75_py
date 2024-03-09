class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        if str1 + str2 != str2 + str1:
            return ""
        length_gcd = gcd(len(str1), len(str2))
        return str1[:length_gcd]

str1 = input("Enter the first string ")
str2 = input("Enter the second string ")

solution = Solution()
result = solution.gcdOfStrings(str1, str2)

print( result)