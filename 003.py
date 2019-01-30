class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        max_len = 0
        sub_str = ""
        start = 0
        index = 0
        while(index <= len(s)):
            # print("start:", start,"index:",index,"substr:", s[start:index], "find:", s[index-1], "len:",index-start)
            finded = sub_str.find(s[index])
            if finded >= 0:
                # 有重复
                if index-start > max_len:
                    max_len = index-start
                start = start + finded + 1
                print('start更新:', start)
            index+=1
        return max_len



# print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring(" "))




 