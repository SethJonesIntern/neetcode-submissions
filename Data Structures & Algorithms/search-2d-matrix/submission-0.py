class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        l = 0
        r = len(matrix) - 1

        cur = -1
        while (l <= r):
            mid = (l + r)//2

            if matrix[mid][0] == target:
                return True

            if matrix[mid][0] > target:
                if mid == 0:
                    return False
                if matrix[mid - 1][0] <= target:
                    cur = mid - 1
                    break
                else:
                    r = mid - 1
            if matrix[mid][0] < target:
                l = mid + 1
            
        l = 0
        r = len(matrix[cur]) - 1


        while(l <= r):
            mid = (l + r)//2
            if matrix[cur][mid] == target:
                return True
            if matrix[cur][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False


