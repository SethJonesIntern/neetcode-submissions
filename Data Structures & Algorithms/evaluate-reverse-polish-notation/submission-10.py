class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []



        for token in tokens:
            if token not in ["+","-","*","/"]:
                stack.append(int(token))
                continue
            num2 = stack.pop()
            num1 = stack.pop()
            if token == "+":
                stack.append(num1 + num2)
            if token == "-":
                stack.append(num1 - num2)
            if token == "*":
                stack.append(num1 * num2)
            if token == "/":
                sign = 1
                if(num1 < 0) != (num2 < 0):
                    sign *= -1
                stack.append((abs(num1) // abs(num2))*sign)
                      

        return stack[0]    