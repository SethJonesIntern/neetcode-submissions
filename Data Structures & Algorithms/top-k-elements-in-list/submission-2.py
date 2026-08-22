import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #counting
        smap = {}
        for num in nums:
            if num in smap:
                smap[num] += 1
            else: smap[num] = 1


        #building bucket/heap
        heap = []
        for num in smap:
            temp = (-smap[num],num)
            heapq.heappush(heap,temp)
        



        #popping heap into res and returning res
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])         
        return res