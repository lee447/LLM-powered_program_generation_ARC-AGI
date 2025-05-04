from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    template = [(0,2),(0,3),(1,0),(1,1),(2,2)]
    center = (1,2)
    out = [[1]*w for _ in range(h)]
    cols = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v!=1:
                cols.setdefault(v, []).append((r,c))
    for v, pts in cols.items():
        rs = [r for r,_ in pts]; cs = [c for _,c in pts]
        mn_r, mx_r, mn_c, mx_c = min(rs), max(rs), min(cs), max(cs)
        cr = (mn_r+mx_r+1)//2; cc = (mn_c+mx_c+1)//2
        or0, oc0 = cr-center[0], cc-center[1]
        for dr,dc in template:
            r2, c2 = or0+dr, oc0+dc
            if 0<=r2<h and 0<=c2<w:
                out[r2][c2] = v
    return out