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
    cy = H/2
    cx = W/2
    angs = []
    for (r,c) in pts:
        y = r+0.5 - cy
        x = c+0.5 - cx
        angs.append(math.atan2(y, x)%(2*math.pi))
    paired = list(zip(angs, pts))
    paired.sort()
    angs = [a for a,_ in paired]
    pts = [p for _,p in paired]
    # find the largest angular gap
    max_gap = -1
    idx = 0
    for i in range(n):
        j = (i+1)%n
        gap = (angs[j] - angs[i]) % (2*math.pi)
        if gap > max_gap:
            max_gap = gap
            idx = i
    # bisector of the gap
    a1 = angs[idx]
    a2 = (angs[(idx+1)%n] + 2*math.pi) if (idx+1)<=idx else angs[(idx+1)%n]
    mid = ((a1 + a2)/2) % (2*math.pi)
    sel = set()
    for a,p in zip(angs, pts):
        d = (a - mid) % (2*math.pi)
        if d>math.pi/2 and d<3*math.pi/2:
            sel.add(p)
    out = [row[:] for row in grid]
    for (r,c) in sel:
        out[r][c]=8; out[r][c+1]=8; out[r+1][c]=8; out[r+1][c+1]=8
    return out