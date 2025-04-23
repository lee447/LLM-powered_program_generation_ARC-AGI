def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    res = [row[:] for row in grid]
    frames = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not visited[i][j]:
                stack = [(i,j)]
                comp = []
                visited[i][j]=True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==5:
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                rs = [r for r,c in comp]; cs = [c for r,c in comp]
                r1, r2 = min(rs), max(rs)
                c1, c2 = min(cs), max(cs)
                # check rectangle border
                ok = True
                for c in range(c1, c2+1):
                    if grid[r1][c]!=5 or grid[r2][c]!=5: ok=False
                for r in range(r1, r2+1):
                    if grid[r][c1]!=5 or grid[r][c2]!=5: ok=False
                if ok:
                    frames.append((r1, r2, c1, c2))
    for r1, r2, c1, c2 in frames:
        for rr in range(r1+1, r2):
            for cc in range(c1+1, c2):
                if res[rr][cc]==0:
                    res[rr][cc]=2
    for r1, r2, c1, c2 in frames:
        stripe_row = r1-1
        if stripe_row<0: continue
        stripe_len = (r2 - r1 + 1) + 1
        start = c1 - stripe_len + 1
        if start < 0: start = 0
        end = start + stripe_len - 1
        if end >= w:
            end = w-1
            start = end - stripe_len + 1
            if start < 0: start = 0
        for cc in range(start, end+1):
            if res[stripe_row][cc]==0:
                res[stripe_row][cc]=2
    return res