from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    r, c = len(grid), len(grid[0])
    def rot180(mat):
        return [row[::-1] for row in mat[::-1]]
    def hmirror(mat):
        return [row[::-1] for row in mat]
    def vmirror(mat):
        return mat[::-1]
    TL = rot180(grid)
    TR = hmirror(TL)
    BL = vmirror(TL)
    BR = rot180(TL)
    out = [[0] * (c * 2) for _ in range(r * 2)]
    for i in range(r):
        for j in range(c):
            out[i][j] = TL[i][j]
            out[i][j + c] = TR[i][j]
            out[i + r][j] = BL[i][j]
            out[i + r][j + c] = BR[i][j]
    return out