class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper = "+-*/"
        for i in tokens:
            if i in oper:
                two, one = stack.pop(), stack.pop()
                if i == "+":
                    stack.append(one + two)
                elif i == "/":
                    stack.append(int(one / two))
                elif i == "*":
                    stack.append(int(one * two))
                else:
                    stack.append(one - two)
            else:
                stack.append(int(i))
        return stack.pop()