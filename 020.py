class Solution:
    def isValid(self, s: str) -> bool:
        queue = list()
        dic = {")":"(","]":"[","}":"{"}
        for x in s:
            if x in "([{":
                queue.append(x)
            else:
                if len(queue) == 0:
                    return False
                if dic[x] != queue.pop():
                    return False
        return len(queue) == 0
        