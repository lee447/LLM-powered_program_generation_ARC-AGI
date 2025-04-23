from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    pts = [(r,c) for r in range(H) for c in range(W) if grid[r][c]==8]
    rs = [r for r,_ in pts]; cs = [c for _,c in pts]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    pattern = [row[c0:c1+1] for row in grid[r0:r1+1]]
    ph, pw = len(pattern), len(pattern[0])
    pat = [[1 if pattern[i][j]==8 else 0 for j in range(pw)] for i in range(ph)]
    out = [row[:] for row in grid]
    for i in range(H-ph+1):
        for j in range(W-pw+1):
            ok = True
            fill = False
            for di in range(ph):
                for dj in range(pw):
                    if pat[di][dj]:
                        v = out[i+di][j+dj]
                        if v not in (0,8):
                            ok = False; break
                        if v==0:
                            fill = True
                if not ok:
                    break
            if ok and fill:
                for di in range(ph):
                    for dj in range(pw):
                        if pat[di][dj] and out[i+di][j+dj]==0:
                            out[i+di][j+dj] = 8
    return out