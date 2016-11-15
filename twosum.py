"""
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = []
        for i in range(len(nums)-1):
            print 'i=', i
            print 'j range:', range(i+1, len(nums))
            for j in range(i+1, len(nums)):
                print 'j=', j
                if nums[i]+nums[j] == target:
                    index = [i, j]
                    break
        return index

if __name__ == '__main__':
    so = Solution()
    nums = [0, 4, 3, 0]
    target = 0
    print so.twoSum(nums, target)
