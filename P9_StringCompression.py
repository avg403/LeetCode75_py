class Solution:
    def compress(self, chars: list[str]) -> int:
        i, w = 0, 0
        while i < len(chars):
            count = 1
            j = i + 1
            while j < len(chars) and chars[i] == chars[j]:
                count += 1
                j += 1
            chars[w] = chars[i]
            w += 1
            if count > 1:
                for digit in str(count):
                    chars[w] = digit
                    w += 1
            i = j
        return w
solution = Solution()
chars = ["a", "a", "b", "b", "c", "c", "c"]
print(solution.compress(chars))
print(chars) 