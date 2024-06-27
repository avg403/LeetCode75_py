class Solution:
    def maxOperations(self,nums:list[int],k:int)->int:
        nums.sort()
        left=0
        right=len(nums)-1
        count=0
        while left<right:
            if (nums[left]+nums[right]==k):
                count+=1
                left+=1
                right-=1
            elif(nums[left]+nums[right]<k):
                left+=1
            else :
                right-=1
        return count
    
solution = Solution()
print(solution.maxOperations([1,2,3,4],5)) 
