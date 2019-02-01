#! python3
#! encoding:UTF-8
# 未完成
class Solution:
    def calc(self, opera, numA, numB):
        ops = {'+': lambda a,b: a+b,'-': lambda a, b: a-b,'*': lambda a, b: a*b, '/': lambda a,b:a/b}
        return ops[opera](int(numA),int(numB))
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1:
            return int(tokens[0])
        if len(tokens) == 3:
            print('最后三个元素', tokens)
            return self.calc(tokens[2], tokens[0], tokens[1])
        elif tokens[-2] in '+-*/':
            # 倒数第二位是操作符，公式： x0 xn (剩余元素) = 
            print('倒数第二位是操作符', tokens)
            return self.calc(tokens[-1], tokens[0], self.evalRPN(tokens[1:-1]))
        else:
            # 倒数第二位是数字
            print('倒数第二位是数字', tokens)
            return self.calc(tokens[-1], self.evalRPN(tokens[:-2]), tokens[-2])

l = ["4","-2","/","2","-3","-","-"]
Solution().evalRPN(l)


["4","-2","/","2","-3","-","-"]
"4","-2","/","2","-3","-","-"
4 - ("-2","/","2","-3","-")
4 - (-2 - ("/","2","-3"))
4 - (-2 - ("/","2","-3"))


