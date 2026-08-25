class Solution:
    def isValid(self, s: str) -> bool:
        working = []
        for char in s:
            if char == '{' or char == '(' or char == '[':
                working.append(char)
            elif len(working) == 0: return False
            if char == '}':
                cur = working.pop()
                if cur != '{':
                    return False
            if char == ']':
                cur = working.pop()
                if cur != '[':
                    return False
            if char == ')':
                cur = working.pop()
                if cur != '(':
                    return False
        if len(working) != 0: return False
        return True

        