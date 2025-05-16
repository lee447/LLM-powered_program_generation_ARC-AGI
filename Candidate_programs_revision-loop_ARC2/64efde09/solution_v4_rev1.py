from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = max({c:0 for row in grid for c in row}, key=lambda c: sum(row.count(c) for row in grid))
    walls = 4
    rows = sorted({y for y in range(h) for x in range(w) if grid[y][x]==walls})
    cols = sorted({x for y in range(h) for x in range(w) if grid[y][x]==walls})
    hr = [ -1 ] + [r for r in rows] + [h]
    hc = [ -1 ] + [c for c in cols] + [w]
    blocks = []
    for i in range(len(hr)-1):
        for j in range(len(hc)-1):
            r0, r1 = hr[i]+1, hr[i+1]
            c0, c1 = hc[j]+1, hc[j+1]
            pts = [(y,x) for y in range(r0,r1) for x in range(c0,c1) if grid[y][x]!=bg and grid[y][x]!=walls]
            if len(pts)==1:
                y,x = pts[0]
                c = grid[y][x]
                for xx in range(c0,c1):
                    if grid[y][xx]!=walls:
                        grid[y][xx]=c
                for yy in range(r0,r1):
                    if grid[yy][x]!=walls:
                        grid[yy][x]=c
    return grid