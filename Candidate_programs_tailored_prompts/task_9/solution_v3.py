def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not seen[i][j]:
                stack = [(i,j)]
                comp = []
                seen[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==5:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,c in comp]
                cs = [c for r,c in comp]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                top_count = sum(1 for r,c in comp if r==r0)
                bot_count = sum(1 for r,c in comp if r==r1)
                if top_count < (c1-c0+1):
                    stripe_r = r0-1
                else:
                    stripe_r = r1+1
                start_c, end_c = c0+1, c1-1
                for c in range(start_c, end_c+1):
                    if 0<=stripe_r<h and 0<=c<w:
                        out[stripe_r][c] = 2
                if (r1-r0+1)==4 and (c1-c0+1)==4:
                    for r in (r0+1, r0+2):
                        for c in (c0+1, c0+2):
                            out[r][c] = 2
    return out