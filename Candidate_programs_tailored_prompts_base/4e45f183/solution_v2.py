def solve(grid):
    H, W = len(grid), len(grid[0])
    zr = [i for i in range(H) if all(c == 0 for c in grid[i])]
    zc = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    brs = [zr[i] + 1 for i in range(len(zr) - 1)]
    bcs = [zc[i] + 1 for i in range(len(zc) - 1)]
    B = len(brs)
    blocks = []
    for bi in range(B):
        r0, r1 = zr[bi] + 1, zr[bi+1]
        for bj in range(B):
            c0, c1 = zc[bj] + 1, zc[bj+1]
            blocks.append((bi, bj, r0, r1, c0, c1))
    # find global motif: largest 8‐conn component of any nonzero color
    from collections import deque
    vis = [[False]*W for _ in range(H)]
    best = []
    best_color = None
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not vis[i][j]:
                col = grid[i][j]
                comp = []
                q = deque([(i,j)])
                vis[i][j] = True
                while q:
                    x,y = q.popleft()
                    comp.append((x,y))
                    for dx in (-1,0,1):
                        for dy in (-1,0,1):
                            nx,ny = x+dx, y+dy
                            if 0 <= nx < H and 0 <= ny < W and not vis[nx][ny] and grid[nx][ny]==col:
                                vis[nx][ny]=True
                                q.append((nx,ny))
                if len(comp) > len(best):
                    best = comp
                    best_color = col
    if not best:
        return grid
    # normalize motif
    minr = min(x for x,y in best)
    minc = min(y for x,y in best)
    motif = [(x-minr, y-minc) for x,y in best]
    mh = max(r for r,c in motif) + 1
    mw = max(c for r,c in motif) + 1
    # clear all old
    for i in range(H):
        for j in range(W):
            if grid[i][j] == best_color:
                grid[i][j] = 0
    # redraw in each block at top‐left corner
    for bi, bj, r0, r1, c0, c1 in blocks:
        for dr, dc in motif:
            grid[r0+dr][c0+dc] = best_color
    return grid