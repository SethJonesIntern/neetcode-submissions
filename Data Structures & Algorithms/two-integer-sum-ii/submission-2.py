class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) -1
        res = []
        while l < r:
            cur = numbers[l] + numbers[r]
            if cur == target:
                res.append(l + 1)
                res.append(r + 1)
                return res
            if cur < target:
                l += 1
            else: r -= 1
        

        