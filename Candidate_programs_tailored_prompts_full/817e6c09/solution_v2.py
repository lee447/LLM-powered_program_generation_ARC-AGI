def solve(grid):
    h, w = len(grid), len(grid[0])
    blocks = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                blocks.append((r, c))
    rs = sorted(r for r, c in blocks)
    cs = sorted(c for r, c in blocks)
    mr = rs[len(rs)//2]
    mc = cs[len(cs)//2]
    bucket = {'NW':[], 'NE':[], 'SW':[], 'SE':[]}
    for r, c in blocks:
        dr, dc = r-mr, c-mc
        if dr<0 and dc<0: bucket['NW'].append((r,c))
        elif dr<0 and dc>0: bucket['NE'].append((r,c))
        elif dr>0 and dc<0: bucket['SW'].append((r,c))
        elif dr>0 and dc>0: bucket['SE'].append((r,c))
    recolor = set()
    for b, pts in bucket.items():
        if len(pts)>2:
            for p in pts:
                recolor.add(p)
    out = [row[:] for row in grid]
    for r, c in recolor:
        out[r][c]=out[r][c+1]=out[r+1][c]=out[r+1][c+1]=8
    return out