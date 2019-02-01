#! python3
#! encoding:UTF-8
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = {'+': lambda a,b: a+b,'-': lambda a, b: a-b,'*': lambda a, b: a*b, '/': lambda a,b:int(a/b)}
        stack = list()
        for a in tokens:
            if a in '+-*/':
                numR = stack.pop()
                numL = stack.pop()
                stack.append(ops[a](numL, numR))
            else:
                stack.append(int(a))
        return stack.pop()

l = ["4","-2","/","2","-3","-","-"]
print(Solution().evalRPN(l))


