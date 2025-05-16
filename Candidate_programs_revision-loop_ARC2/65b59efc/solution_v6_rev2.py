from typing import List
from collections import Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    colors = set(x for row in grid for x in row)
    fence = None
    for c in colors:
        row_count = sum(1 for i in range(n) if sum(1 for v in grid[i] if v == c) > m // 2)
        col_count = sum(1 for j in range(m) if sum(1 for i in range(n) if grid[i][j] == c) > n // 2)
        if row_count > 1 and col_count > 1:
            fence = c
            break
    row_f = [i for i in range(n) if sum(1 for v in grid[i] if v == fence) > m // 2]
    col_f = [j for j in range(m) if sum(1 for i in range(n) if grid[i][j] == fence) > n // 2]
    rk = [0] + row_f + [n]
    ck = [0] + col_f + [m]
    R, C = len(rk) - 1, len(ck) - 1
    bh = max(rk[i+1] - rk[i] - 1 for i in range(R))
    bw = max(ck[j+1] - ck[j] - 1 for j in range(C))
    out = [[0] * (bw * C) for _ in range(bh * R)]
    for br in range(R):
        for bc in range(C):
            r0, c0 = rk[br] + 1, ck[bc] + 1
            cnt = Counter()
            mask = [[0] * bw for _ in range(bh)]
            for i in range(bh):
                for j in range(bw):
                    ri, cj = r0 + i, c0 + j
                    if ri < n and cj < m:
                        v = grid[ri][cj]
                        if v != fence and v != 0:
                            cnt[v] += 1
                            mask[i][j] = 1
            if cnt:
                color = max(cnt, key=cnt.get)
                for i in range(bh):
                    for j in range(bw):
                        if mask[i][j]:
                            out[br*bh + i][bc*bw + j] = color
    return out