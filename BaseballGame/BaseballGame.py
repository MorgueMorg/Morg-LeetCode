class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        count = 0
        for i in ops:
            if i == "C":
                count -= stack.pop()
            elif i == "D":
                stack.append(stack[-1] * 2)
                count += stack[-1]
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
                count += stack[-1]
            else:
                stack.append(int(i))     
                count += stack[-1]
        return count


