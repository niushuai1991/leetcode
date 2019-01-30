#! python3
class Solution:
    def _way(self,input):
        ops = {'+': lambda a,b: a+b,
                '-': lambda a, b: a-b,
                '*': lambda a, b: a*b}
        res = []
        for i, c in enumerate(input):
            if c in '+-*':
                left = input[:i]
                right = input[i+1:]
                left_list = self._way(left)
                right_list = self._way(right)
                for x in left_list:
                    for y in right_list:
                        res.append(ops[c](x,y))
        if len(res) == 0:
            res.append(int(input))
        return res
    def diffWaysToCompute(self, input):
        return self._way(input)
if __name__ == '__main__':
    l = Solution().diffWaysToCompute('3+4*5')
    for r in l:
        print(r, " ")