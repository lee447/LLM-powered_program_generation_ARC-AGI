import math

def solve(grid):
    h, w = len(grid), len(grid[0])
    blocks = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                blocks.append((r, c))
    if not blocks:
        return grid
    rs = [r for r,c in blocks]
    cs = [c for r,c in blocks]
    cr = sum(rs)/len(rs) + 0.5
    cc = sum(cs)/len(cs) + 0.5
    angles = []
    for r,c in blocks:
        dr = r+0.5 - cr
        dc = c+0.5 - cc
        a = math.atan2(dr, dc) % (2*math.pi)
        d2 = dr*dr + dc*dc
        angles.append((r, c, a, d2))
    bins = {i:[] for i in range(4)}
    for item in angles:
        a = item[2]
        idx = int(a / (math.pi/2)) % 4
        bins[idx].append(item)
    to_highlight = set()
    for grp in bins.values():
        if len(grp) >= 2:
            grp.sort(key=lambda x: x[3], reverse=True)
            for r, c, *_ in grp[:2]:
                to_highlight.add((r, c))
    out = [row[:] for row in grid]
    for r, c in to_highlight:
        for dr in (0,1):
            for dc in (0,1):
                out[r+dr][c+dc] = 8
    return out