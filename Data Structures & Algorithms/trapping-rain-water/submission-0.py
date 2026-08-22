class Solution:
    def trap(self, height: List[int]) -> int:
        
        length = len(height)

        L = [0] * length
        R = [0] * length
        res = 0


        curmaxl = 0
        curmaxr = 0

        for i in range(length):

            curmaxl = max(curmaxl, height[i])
            curmaxr = max(curmaxr, height[length - i - 1])

            R[length - i - 1] = curmaxr
            L[i] = curmaxl

        for i in range(length):
            if height[i] < min(L[i],R[i]):
                res += min(L[i],R[i]) - height[i]

        return res








