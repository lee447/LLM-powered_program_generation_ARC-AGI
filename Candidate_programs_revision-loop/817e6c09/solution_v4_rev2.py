import math
def solve(grid):
    H, W = len(grid), len(grid[0])
    pts = []
    for r in range(H-1):
        for c in range(W-1):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                pts.append((r,c))
    n = len(pts)
    if n==0:
        return grid
    cy, cx = H/2, W/2
    angs = []
    for r,c in pts:
        y = r+0.5 - cy
        x = c+0.5 - cx
        angs.append(math.atan2(y, x) % (2*math.pi))
    paired = sorted(zip(angs, pts))
    angs, pts = zip(*paired)
    angs = list(angs)
    pts = list(pts)
    max_gap = -1
    idx = 0
    for i in range(n):
        j = (i+1)%n
        gap = (angs[j] - angs[i]) % (2*math.pi)
        if gap > max_gap:
            max_gap = gap
            idx = i
    bis = (angs[idx] + max_gap/2) % (2*math.pi)
    sel = set()
    for a,p in zip(angs, pts):
        d = (a - bis) % (2*math.pi)
        if d > math.pi/2 and d < 3*math.pi/2:
            sel.add(p)
    out = [row[:] for row in grid]
    for r,c in sel:
        out[r][c]=8; out[r][c+1]=8; out[r+1][c]=8; out[r+1][c+1]=8
    return out