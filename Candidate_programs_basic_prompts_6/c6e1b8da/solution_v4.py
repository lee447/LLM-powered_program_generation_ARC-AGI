from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [[0]*w for _ in range(h)]
    colors = set(c for row in grid for c in row if c!=0)
    for col in colors:
        pts = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==col]
        rs = [r for r,_ in pts]; cs = [c for _,c in pts]
        r0,r1,minc,maxc = min(rs), max(rs), min(cs), max(cs)
        row_counts = {r:0 for r in range(r0,r1+1)}
        col_counts = {c:0 for c in range(minc,maxc+1)}
        for r,c in pts:
            row_counts[r]+=1; col_counts[c]+=1
        maxr = max(row_counts.values()); maxc_cnt = max(col_counts.values())
        t_row = sum(1 for v in row_counts.values() if v==maxr)
        t_col = sum(1 for v in col_counts.values() if v==maxc_cnt)
        t = min(t_row, t_col)
        for c in range(minc, maxc+1):
            for r in range(r0, r0+t):
                res[r][c] = col
        for r in range(r0, r1+1):
            for c in range(minc, minc+t):
                res[r][c] = col
    return res