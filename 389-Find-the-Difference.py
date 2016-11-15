class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        array = []
        for i in range(len(t)):
            if t[i] not in array:
                if t.count(t[i]) >s.count(t[i]):
                    return t[i]
                    
