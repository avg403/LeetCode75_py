class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result=[]
        largest=max(candies)
        for i in range(len(candies)):
            updated_candies=candies[i]+extraCandies
            if updated_candies<largest:
                result.append(False)
            else:
                result.append(True)
        return result
solution = Solution()
output = solution.kidsWithCandies([2, 3, 5, 1, 3], 3)
print( output)