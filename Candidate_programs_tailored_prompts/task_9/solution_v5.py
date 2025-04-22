def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not seen[i][j]:
                # flood-fill component
                stack = [(i,j)]
                comp = []
                seen[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==5:
                            seen[nr][nc]=True
                            stack.append((nr,nc))
                rs = [r for r,c in comp]
                cs = [c for r,c in comp]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                height = r1-r0+1
                width = c1-c0+1
                # determine open side
                top_open = all(grid[r0][c]==0 for c in range(c0+1, c1))
                bot_open = all(grid[r1][c]==0 for c in range(c0+1, c1))
                # stripe
                inner_w = max(0, (c1-c0-1))
                if inner_w>0:
                    start_c = c0+1
                    if top_open:
                        sr = r0-1
                    elif bot_open:
                        sr = r1+1
                    else:
                        sr = None
                    if sr is not None and 0<=sr<h:
                        for k in range(inner_w):
                            c = start_c + k
                            if 0<=c<w:
                                out[sr][c] = 2
                # center fill for 4x4 frame
                if height==4 and width==4:
                    for dr in (1,2):
                        for dc in (1,2):
                            rr = r0+dr
                            cc = c0+dc
                            out[rr][cc] = 2
    return out