def solve(grid):
    H = len(grid)
    W = len(grid[0])
    visited = [[False]*W for _ in range(H)]
    ccs = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                cc = []
                while stack:
                    x,y = stack.pop()
                    cc.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] != 0:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                ccs.append(cc)
    region = max(ccs, key=lambda cc: len(cc))
    outside_ccs = [cc for cc in ccs if cc is not region]
    region_set = set(region)
    counts = {}
    for x,y in region:
        v = grid[x][y]
        counts[v] = counts.get(v,0) + 1
    B = max(counts.items(), key=lambda kv: kv[1])[0]
    interior = [v for v in counts if v != B]
    mapping = {}
    for c in interior:
        for cc in outside_ccs:
            vals = {grid[x][y] for x,y in cc}
            if c in vals:
                d = (vals - {c}).pop()
                mapping[c] = d
                break
    rows = [x for x,_ in region]
    cols = [y for _,y in region]
    r0,r1 = min(rows), max(rows)
    c0,c1 = min(cols), max(cols)
    h = r1 - r0 + 1
    w = c1 - c0 + 1
    res = [[B]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            x,y = r0+i, c0+j
            v = grid[x][y] if (x,y) in region_set else 0
            if v in mapping:
                res[i][j] = mapping[v]
            else:
                res[i][j] = B
    return res