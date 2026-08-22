class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        temp = 1
        for i in range(len(nums)):
            res.append(temp)
            temp *= nums[i]

        temp = 1
        for i in range(len(nums)):
           res[len(nums) - 1 - i] *= temp
           temp *= nums[len(nums) - i - 1]
        return res

        