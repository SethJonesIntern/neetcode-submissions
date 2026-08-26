class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i],speed[i]))
        pairs = sorted(pairs)

        stack = []

        for i in range(len(pairs)):

            #Time to destination
            cur = (target - pairs[i][0])/pairs[i][1]

            #if stack empty, add cur and continue
            if len(stack) == 0:
                stack.append(cur)
                continue
            

            #if stack not empty, record top element
            last = stack.pop()


            #while cur is > last element, pop last element and update last

            while stack and cur >= last:
                last = stack.pop()

            
            #if while loop ends and cur is still greater than last, it means list is empty AND cur is still greater, list is now of size 1, only element is cur
                
            if(cur >= last):
                stack.append(cur)
                continue


            #if cur < last then both 
            
            stack.append(last)
            stack.append(cur)
        return len(stack)
        