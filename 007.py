class Solution:
    def reverse(self, x: 'int') -> 'int':
        positive = x > 0
        x = abs(x)
        num = 0
        while x > 0:
            num = num*10 + (x%10)
            x = x // 10
        if num < (-2**31) or num > (2**31-1):
            return 0
        if positive:
            return num
        else:
            return -num