class Solution:
    def flipAndInvertImage(self, A: 'List[List[int]]') -> 'List[List[int]]':
        l = list()
        for x in A:
            l.append([a^1 for a in x[::-1]])
        return l