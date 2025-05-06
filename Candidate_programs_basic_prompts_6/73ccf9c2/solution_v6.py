def solve(grid):
    H, W = len(grid), len(grid[0])
    # find the nonzero color
    col = 0
    for row in grid:
        for v in row:
            if v != 0:
                col = v
                break
        if col:
            break
    # flood fill to get components
    vis = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == col and not vis[i][j]:
                stack = [(i,j)]
                vis[i][j] = True
                comp = []
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not vis[nx][ny] and grid[nx][ny] == col:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                min_i = min(x for x,y in comp)
                max_i = max(x for x,y in comp)
                min_j = min(y for x,y in comp)
                max_j = max(y for x,y in comp)
                h = max_i - min_i + 1
                w = max_j - min_j + 1
                comps.append({
                    "comp": comp,
                    "min_i": min_i, "max_i": max_i,
                    "min_j": min_j, "max_j": max_j,
                    "h": h, "w": w,
                    "len": len(comp)
                })
    # count dims occurrences (excluding dims with 1)
    from collections import Counter
    dims = [(c["h"], c["w"]) for c in comps if c["h"]>1 and c["w"]>1]
    cnt = Counter(dims)
    if not cnt:
        return [[]]
    mc = max(cnt.values())
    cands = [d for d,v in cnt.items() if v==mc]
    # pick dims with minimal area
    best_dim = min(cands, key=lambda d: d[0]*d[1])
    bh, bw = best_dim
    # among comps matching dims pick max len
    sel = [c for c in comps if c["h"]==bh and c["w"]==bw]
    sel = max(sel, key=lambda c: c["len"])
    i0, i1, j0, j1 = sel["min_i"], sel["max_i"], sel["min_j"], sel["max_j"]
    out = []
    for i in range(i0, i1+1):
        row = []
        for j in range(j0, j1+1):
            row.append(grid[i][j] if grid[i][j]==col else 0)
        out.append(row)
    return out