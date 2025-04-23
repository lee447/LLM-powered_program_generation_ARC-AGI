from typing import List
from collections import Counter
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    row_nonzero = [any(grid[r][c] != 0 for c in range(m)) for r in range(n)]
    col_nonzero = [any(grid[r][c] != 0 for r in range(n)) for c in range(m)]
    row_ranges, col_ranges = [], []
    r = 0
    while r < n:
        if row_nonzero[r]:
            start = r
            while r < n and row_nonzero[r]:
                r += 1
            row_ranges.append((start, r - 1))
        else:
            r += 1
    c = 0
    while c < m:
        if col_nonzero[c]:
            start = c
            while c < m and col_nonzero[c]:
                c += 1
            col_ranges.append((start, c - 1))
        else:
            c += 1
    blocks = []
    for bi, (rs, re) in enumerate(row_ranges):
        for bj, (cs, ce) in enumerate(col_ranges):
            block = [grid[i][cs:ce+1] for i in range(rs, re+1)]
            blocks.append((bi, bj, block))
    bh = row_ranges[0][1] - row_ranges[0][0] + 1
    bw = col_ranges[0][1] - col_ranges[0][0] + 1
    result = [[0]*m for _ in range(n)]
    for bi, bj, block in blocks:
        cnt = Counter(v for row in block for v in row if v != 0)
        if len(cnt) <= 1:
            ti, tj = bi, bj
        else:
            mc = min(cnt, key=cnt.get)
            pts = [(i,j) for i,row in enumerate(block) for j,v in enumerate(row) if v==mc]
            si = sum(i for i,j in pts)/len(pts)
            sj = sum(j for i,j in pts)/len(pts)
            if si < bh/3:
                ti = 0
            elif si > bh*2/3:
                ti = 2
            else:
                ti = 1
            if sj < bw/3:
                tj = 0
            elif sj > bw*2/3:
                tj = 2
            else:
                tj = 1
        rs, re = row_ranges[ti]
        cs, ce = col_ranges[tj]
        for i in range(re-rs+1):
            for j in range(ce-cs+1):
                result[rs+i][cs+j] = block[i][j]
    return result