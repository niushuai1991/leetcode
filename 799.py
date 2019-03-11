class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 初始化所有的杯子
        g = [[0] * k for k in range(1, 102, 1)]
        # 开始倒酒，计算倒酒后每个杯子内的酒
        g[0][0] = poured
        for r in range(query_row+1):
            for c in range(r+1):
                if g[r][c] < 1:
                    continue
                ll = (g[r][c]-1) / 2
                g[r][c]=1
                if ll > 0:
                    g[r+1][c] += ll
                    g[r+1][c+1] += ll
        # 返回指定杯子里的酒量
        return g[query_row][query_glass]