class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i,temp in enumerate(temperatures):
            #if len(stack) == 0 or temp < stack[len(stack) -1]:
                #stack.append((i,temp))
               # res.append(0)
                #continue
            
            res. append(0)
            while(stack and temp > stack[len(stack) - 1][1]):
                count, whocares = stack.pop()
                res[count] = i - count
            stack.append((i,temp))
        return res

        