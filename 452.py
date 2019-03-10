class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        # 1.排序
        points = sorted(points)
        # 2.找到第一个点的开始点和结束点
        end = points[0][1]
        num = 1
        # 3.遍历所有的点
        for s,e in points[1:]:
            # 如果结束点大于新气球的开始点
            if end >= s:
                end = min(end, e)
            else:
                num+=1
                end = e
        return num