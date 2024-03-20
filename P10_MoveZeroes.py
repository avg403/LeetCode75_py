class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j = 0  
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]  
                j += 1  

solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)  