#! python3
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = dict()
        for s in strs:
            # 先对str进行排序，然后检查是否在dic中存在
            sortedStr = tuple(sorted(s))
            if sortedStr in dic.keys():
                dic[sortedStr].append(s)
            else:
                dic[sortedStr]=[s]
        return dic.values()
l = ["eat","tea","tan","ate","nat","bat"]
groupList = Solution().groupAnagrams(l)
for li in groupList:
    print(li)