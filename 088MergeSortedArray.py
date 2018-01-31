#!/usr/bin/python3

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        n1_index = 0
        n2_index = 0
        while n > n2_index:
            if m == n1_index - n2_index:
                # nums1已经到头了
                #print('nums1已经到头了')
                nums1.insert(n1_index, nums2[n2_index])
                n1_index = n1_index + 1
                n2_index = n2_index + 1
                continue
            # print('---------------')
            # print(n1_index,n2_index)
            # print(nums1[n1_index], nums2[n2_index])
            if nums1[n1_index] > nums2[n2_index]:
                # 当前n1的值比n2大 将标nums2的值插入到nums1中
                #print('当前n1的值比n2大 将标nums2的值插入到nums1中')
                nums1.insert(n1_index, nums2[n2_index])
                n1_index = n1_index + 1
                n2_index = n2_index + 1
            else:
                # 当前n1的值小于n2，则n2_index + 1
                #print('当前n1的值小于n2，则n2_index + 1')
                n1_index = n1_index + 1
        while len(nums1) != m+n:
            nums1.pop()

if __name__ == '__main__':
    nums1 = [0]
    nums2 =  [2, 4, 7]
    Solution().merge(nums1, 0, nums2,len(nums2))
    print(nums1)
