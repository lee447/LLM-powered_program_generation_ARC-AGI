def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==6 and not seen[i][j]:
                comp = [(i,j)]
                seen[i][j] = True
                stack = [(i,j)]
                while stack:
                    r,c = stack.pop()
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==6:
                            seen[nr][nc]=True
                            comp.append((nr,nc))
                            stack.append((nr,nc))
                if len(comp)>1:
                    rs = [r for r,c in comp]; cs = [c for r,c in comp]
                    mr, Mr = max(rs), min(rs)
                    mc, Mc = max(cs), min(cs)
                    br = max(rs); bc = max(cs)
                    for dr in (0,1):
                        for dc in (0,1):
                            r = br+dr; c = bc+dc
                            if 0<=r<h and 0<=c<w and out[r][c]==0:
                                out[r][c] = 4
    return out