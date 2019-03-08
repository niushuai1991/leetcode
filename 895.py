import collections
class FreqStack:
    
    
    def __init__(self):
        self.counter = dict() # key: 数字 value: 频率
        self.index_list = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, x: int) -> None:
        freq = None
        if x in self.counter:
            self.counter[x] += 1
            freq = self.counter[x]
        else:
            freq = 1
            self.counter[x] = freq
        if freq > self.max_freq:
            self.max_freq = freq
        self.index_list[freq].append(x)
        
    def pop(self) -> int:
        # print(self.counter, self.index_list)
        # 找到最大频率值
        max_freq = self.max_freq
        # 从栈中找到最近的最大频率数
        x = self.index_list[max_freq].pop()
        self.counter[x] -=1
        if not self.index_list[max_freq]:
            # 这个频率为空的时候，删除对应的列表
            # del self.index_list[max_freq]
            self.max_freq -=1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()