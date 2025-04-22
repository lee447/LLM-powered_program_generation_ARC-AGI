def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    used = [[False]*w for _ in range(h)]
    out = [[c for c in row] for row in grid]
    def bfs(sr, sc):
        q = [(sr, sc)]
        comp = {(sr, sc)}
        used[sr][sc] = True
        for r,c in q:
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0<=nr<h and 0<=nc<w and not used[nr][nc] and grid[nr][nc]==5:
                    used[nr][nc]=True
                    comp.add((nr,nc))
                    q.append((nr,nc))
        return comp
    frames = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not used[i][j]:
                comp = bfs(i,j)
                rs = [r for r,_ in comp]
                cs = [c for _,c in comp]
                minr, maxr = min(rs), max(rs)
                minc, maxc = min(cs), max(cs)
                rows = maxr-minr+1
                tops = sum(1 for c in range(minc,maxc+1) if (minr,c) in comp)
                bots = sum(1 for c in range(minc,maxc+1) if (maxr,c) in comp)
                orient = 'upright' if bots>tops else 'upsidedown'
                frames.append((comp,minr,maxr,minc,maxc,orient))
    for comp,minr,maxr,minc,maxc,orient in frames:
        height = maxr-minr+1
        legs = [c for c in range(minc,maxc+1) if sum((r,c) in comp for r in range(minr,maxr+1))==height]
        a,b = min(legs), max(legs)
        if orient=='upright':
            stripe_row = minr-1
            open_row = minr
        else:
            stripe_row = maxr+1
            open_row = maxr
        inner = [c for c in range(a+1,b) if grid[open_row][c]==0]
        for c in inner:
            if 0<=stripe_row<h:
                out[stripe_row][c]=2
        inner_h = maxr-minr-1
        inner_w = maxc-minc-1
        if inner_h==4 and inner_w==4:
            for r in range(minr+1,minr+3):
                for c in range(minc+1,minc+3):
                    out[r][c]=2
    return out