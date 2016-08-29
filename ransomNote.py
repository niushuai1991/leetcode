class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        list = []
        for ran in ransomNote:
            if ran not in list:
                if ran not in magazine:
                    return False
                elif ransomNote.count(ran)>magazine.count(ran):
                    return False
                list.append(ran)
                
        else:
            return True

if __name__ == '__main__':
    print Solution().canConstruct('a','b')
    print Solution().canConstruct('aa','ab')
    print Solution().canConstruct('aa','aab')
    
