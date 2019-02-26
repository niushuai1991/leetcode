class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points = sorted(points)
        # 拿第一个气球的结束点
        end = points[0][1]
        num = 1
        for s, e in points:
            if end >= s:
                # 说明这一轮使用的箭还能射破这个气球
                end = min(end, e)
            else:
                # 说明需要增加一把新的箭来使用
                num+=1
                end = e
        return num