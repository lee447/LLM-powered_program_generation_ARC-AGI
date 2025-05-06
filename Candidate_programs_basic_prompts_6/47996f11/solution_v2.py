def solve(grid):
    h, w = len(grid), len(grid[0])
    target = 6
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    # find the connected component of 6 touching the top border
    from collections import deque
    que = deque()
    for c in range(w):
        if grid[0][c] == target:
            que.append((0,c))
            seen[0][c] = True
    comp = []
    if que:
        while que:
            r,c = que.popleft()
            comp.append((r,c))
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0 <= nr < h and 0 <= nc < w and not seen[nr][nc] and grid[nr][nc] == target:
                    seen[nr][nc] = True
                    que.append((nr,nc))
    if not comp:
        return grid
    # bounding box
    rs = [r for r,c in comp]; cs = [c for r,c in comp]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    H = r1 - r0 + 1; W = c1 - c0 + 1
    # take the block immediately to the right of the hole
    if c1+W < w:
        B = [row[c1+1:c1+1+W] for row in grid[r0:r1+1]]
    else:
        B = [row[c0-W:c0] for row in grid[r0:r1+1]]
    out = [row[:] for row in grid]
    for i in range(H):
        for j in range(W):
            if grid[r0+i][c0+j] == target:
                out[r0+i][c0+j] = B[i][j]
    return out