class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums)<3:
            return False
        first=float('inf')
        second=float('inf')
        for num in nums:
            if num<=first:
                first=num
            elif num<=second:
                second=num
            else:
                return True
        return False
solution = Solution()
print(solution.increasingTriplet([2,1,5,0,4,6]))
