from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        smap = {}

        for num in nums:
            smap[num] = 1

        res = 0
        for num in smap:
            if smap[num] == 1:
                temp = 1
                cur = num
                smap[num] = 0
                while cur + 1 in smap:
                    if smap[cur +1] == 1:
                        cur += 1
                        temp +=1
                        smap[cur] = 0

                cur = num
                while cur - 1 in smap:
                    if smap[cur - 1] == 1:
                        cur -= 1
                        temp += 1
                        smap[cur] = 0
                
                res = max(res,temp)

        return res





