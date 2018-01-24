#!/usr/bin/python3
class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0
        max_substr = []
        substr = []
        count = 0
        for x in s:
            if x in substr:
                # 有重复，复位
                substr = substr[substr.index(x)+1:]
                print('截取后：', substr)
                substr.append(x)
                count = len(substr)
            else:
                # 没有重复，加1
                count = count + 1
                substr.append(x)
            if count > max_count:
                max_count = count
                max_substr = substr[:]
            print(count,substr)
        return max_count, max_substr
if __name__ == '__main__':
    max_count, max_substr = Solution().lengthOfLongestSubstring("abcabcbb")
    assert max_count == 3
    max_count, max_substr = Solution().lengthOfLongestSubstring("ohvhjdml")
    assert max_count == 6
    max_count, max_substr = Solution().lengthOfLongestSubstring("ggububgvfk")
    assert max_count == 6
    print('最大长度：',max_count," 最大子串:",max_substr)
    