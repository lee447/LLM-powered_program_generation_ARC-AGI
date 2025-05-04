def solve(grid):
    h, w = len(grid), len(grid[0])
    anchors = [(i,j) for i in range(h) for j in range(w) if grid[i][j]==4]
    reds = {(i,j) for i in range(h) for j in range(w) if grid[i][j]==2}
    visited = set()
    clusters = []
    for r,c in reds:
        if (r,c) in visited: continue
        stack = [(r,c)]
        comp = set()
        while stack:
            x,y = stack.pop()
            if (x,y) in comp: continue
            comp.add((x,y))
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = x+dx,y+dy
                if (nx,ny) in reds and (nx,ny) not in comp:
                    stack.append((nx,ny))
        visited |= comp
        clusters.append(comp)
    patterns = []
    for comp in clusters:
        cr = sum(x for x,y in comp)/len(comp)
        cc = sum(y for x,y in comp)/len(comp)
        best = None
        bd = None
        for ax,ay in anchors:
            d = abs(ax-cr)+abs(ay-cc)
            if bd is None or d<bd or (d==bd and (abs(ax-cr),abs(ay-cc))<(abs(best[0]-cr),abs(best[1]-cc))):
                bd = d; best = (ax,ay)
        ax,ay = best
        offs = [(x-ax,y-ay) for x,y in comp]
        flipped = [(-dx,-dy) for dx,dy in offs]
        patterns.append(flipped)
    out = [row[:] for row in grid]
    for ax,ay in anchors:
        for patt in patterns:
            for dx,dy in patt:
                x,y = ax+dx, ay+dy
                if 0<=x<h and 0<=y<w and out[x][y]==0:
                    out[x][y] = 2
    return out