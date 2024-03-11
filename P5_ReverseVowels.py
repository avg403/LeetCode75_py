class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        s_vowel=[]
        final=[]

        for i in s:
            if i in vowels:
                s_vowel.append(i)

        j=len(s_vowel)-1

        for i in range(len(s)):
            if s[i] in vowels:
                final.append(s_vowel[j])
                j-=1
            else:
                final.append(s[i])

        return ''.join(final)

solution = Solution()
print(solution.reverseVowels("LeetcOde"))
