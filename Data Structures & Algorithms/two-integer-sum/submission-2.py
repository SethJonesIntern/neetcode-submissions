class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        smap = {}
        for i, x in enumerate(nums):
            if target - x in smap:
                return [min(i, smap[target - x]), max(i, smap[target - x]) ]
            smap[x] = i
        