'''
Created on 2018年1月24日

@author: niushuai
'''


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min_int = -2147483648
        max_int = 2147483647
        print(max_int)
        positive_number = x > 0
        if x < 0:
            x = abs(x)
        reverse_num = 0
        while x != 0:
            num = x % 10
            x = x // 10
            reverse_num = reverse_num * 10 + num
        if reverse_num < min_int or reverse_num > max_int:
            return 0
        if positive_number:
            return reverse_num
        else:
            return -reverse_num


if __name__ == '__main__':
    print('hello')
    print(Solution().reverse(-14264532789))
