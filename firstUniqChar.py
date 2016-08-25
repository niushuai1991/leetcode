
class Solution(object):
    def firstUniqChar(self, s):
        """
        https://leetcode.com/problems/first-unique-character-in-a-string/

        Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

        Examples:

        s = "leetcode"
        return 0.

        s = "loveleetcode",
        return 2.
        Note: You may assume the string contain only lowercase letters.

        Subscribe to see which companies asked this question

        :type s: str
        :rtype: int
        """
        order = []
        index = -1
        for i in range(len(s)):
            if s[i] not in order:
                for o in range(i+1,len(s)):
                    if s[o] == s[i]:
                        order.append(s[i])
                        break
                else:
                    return i                                                
        return index               
            
if __name__ == '__main__':
    print -1 == Solution().firstUniqChar("cc")
    print 0 == Solution().firstUniqChar("leetcode")
    print 0 == Solution().firstUniqChar("1")
    print -1 == Solution().firstUniqChar("aabbccddeea")
    print 8 == Solution().firstUniqChar("aabbccdde")
