def solve(grid):
    H = len(grid)
    W = len(grid[0])
    vals = set()
    for r in grid:
        vals |= set(r)
    fg = None
    for v in vals:
        if v not in (0,) and sum(row.count(v) for row in grid) < H*W:
            if v != 0:
                fg = v if fg is None else fg
    if fg is None:
        fg = 2
    bg_colors = [v for v in vals if v != fg]
    regions = {}
    for bg in bg_colors:
        r0 = H; r1 = -1; c0 = W; c1 = -1
        for i in range(H):
            for j in range(W):
                if grid[i][j] == bg:
                    if i < r0: r0 = i
                    if i > r1: r1 = i
                    if j < c0: c0 = j
                    if j > c1: c1 = j
        regions[bg] = (r0, r1, c0, c1)
    hpart = all(regions[bg][2] == 0 and regions[bg][3] == W-1 for bg in bg_colors)
    vpart = all(regions[bg][0] == 0 and regions[bg][1] == H-1 for bg in bg_colors)
    visited = [[False]*W for _ in range(H)]
    out = [row[:] for row in grid]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == fg and not visited[i][j]:
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == fg:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                r0 = min(x for x,y in comp)
                c0 = min(y for x,y in comp)
                r1 = max(x for x,y in comp)
                c1 = max(y for x,y in comp)
                neigh_bg = None
                for x,y in comp:
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != fg:
                            neigh_bg = grid[nx][ny]
                            break
                    if neigh_bg is not None:
                        break
                if neigh_bg is None:
                    if hpart:
                        if r0 <= min(regions[b][1] for b in bg_colors):
                            lb = [bg for bg in bg_colors if regions[bg][0] == 0][0]
                            neigh_bg = lb
                        else:
                            neigh_bg = [bg for bg in bg_colors if regions[bg][1] == H-1][0]
                    elif vpart:
                        if c0 <= min(regions[b][3] for b in bg_colors):
                            neigh_bg = [bg for bg in bg_colors if regions[bg][2] == 0][0]
                        else:
                            neigh_bg = [bg for bg in bg_colors if regions[bg][3] == W-1][0]
                    else:
                        neigh_bg = bg_colors[0]
                other_bg = [b for b in bg_colors if b != neigh_bg][0]
                r0o,c0o = r0,c0
                w = c1 - c0 + 1
                cmin,cmax = regions[neigh_bg][2], regions[neigh_bg][3]
                if neigh_bg < other_bg:
                    new_c0 = cmax - (w-1)
                else:
                    new_c0 = cmin
                shape = [(x-r0, y-c0) for x,y in comp]
                for x,y in comp:
                    out[x][y] = neigh_bg
                for dr,dc in shape:
                    out[r0+dr][new_c0+dc] = fg
    return out