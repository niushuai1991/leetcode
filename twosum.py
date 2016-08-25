class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index=[]
        for i in range(len(nums)-1):
            print 'i=',i
            print 'j range:',range(i+1,len(nums))
            for j in range(i+1,len(nums)):
                print 'j=',j
                if nums[i]+nums[j] == target:
                    index=[i,j]
                    break;
                
        return index


if __name__ == '__main__':
    so = Solution();
    nums = [0,4,3,0]
    target = 0
    index = so.twoSum(nums,target)
    print index
