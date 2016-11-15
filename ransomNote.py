"""
383. Ransom Note
 Given  an arbitrary  ransom  note  string  and  another  string  containing  letters from  all  the  magazines,  write  a  function  that  will  return  true  if  the  ransom   note  can  be  constructed  from  the  magazines ;  otherwise,  it  will  return  false.   
Each  letter  in  the  magazine  string  can  only  be  used  once  in  your  ransom  note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        order = []
        for ran in ransomNote:
            if ran not in order:
                if ran not in magazine:
                    return False
                elif ransomNote.count(ran) > magazine.count(ran):
                    return False
                order.append(ran)
                
        else:
            return True

if __name__ == '__main__':
    print Solution().canConstruct('a', 'b')
    print Solution().canConstruct('aa', 'ab')
    print Solution().canConstruct('aa', 'aab')
