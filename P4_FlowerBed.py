class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed=[0]+flowerbed+[0]
        count=0
        i=1
        while i<len(flowerbed)-1:
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                count +=1
            i+=1
        return (count>=n)
solution = Solution()
print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))
