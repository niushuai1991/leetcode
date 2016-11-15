import random

class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.array = nums
        self.origin = self.array
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.array = self.origin
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        list = range(len(self.array))
        newarray = []
        while list:
            randint = random.choice(list)
            list.remove(randint)
            newarray.append(self.array[randint])
        self.array = newarray
        return newarray

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

if __name__ == '__main__':
    obj = Solution([1,2,3]);
    param_1 = obj.reset()
    param_2 = obj.shuffle()
    print param_1
    print param_2
    
