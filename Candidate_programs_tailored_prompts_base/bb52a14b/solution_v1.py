def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    seeds = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8:
                cnt4 = 0
                for di,dj in dirs:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == 4:
                        cnt4 += 1
                if cnt4:
                    seeds.append((cnt4, i, j))
    if not seeds:
        return [row[:] for row in grid]
    seeds.sort(reverse=True)
    _, si, sj = seeds[0]
    T = [(di,dj) for di,dj in dirs if 0 <= si+di < h and 0 <= sj+dj < w and grid[si+di][sj+dj] == 4]
    B = [(di,dj) for di,dj in dirs if 0 <= si+di < h and 0 <= sj+dj < w and grid[si+di][sj+dj] == 1]
    anchors = [(i,j) for i in range(h) for j in range(w) if grid[i][j] == 8 and not (i==si and j==sj)]
    # try B match
    for i,j in anchors:
        ok = True
        for di,dj in B:
            ni, nj = i+di, j+dj
            if not (0 <= ni < h and 0 <= nj < w and grid[ni][nj] == 1):
                ok = False
                break
        if not ok:
            continue
        for di,dj in T:
            ni, nj = i+di, j+dj
            if not (0 <= ni < h and 0 <= nj < w) or grid[ni][nj] == 8:
                ok = False
                break
        if ok:
            ti, tj = i, j
            break
    else:
        # fallback: bottom-most candidate with T in-bounds and not overlapping 8
        cand = None
        for i,j in sorted(anchors, key=lambda x:(-x[0],x[1])):
            ok = True
            for di,dj in T:
                ni, nj = i+di, j+dj
                if not (0 <= ni < h and 0 <= nj < w) or grid[ni][nj] == 8:
                    ok = False
                    break
            if ok:
                cand = (i,j)
                break
        if cand is None:
            return [row[:] for row in grid]
        ti, tj = cand
    out = [row[:] for row in grid]
    for di,dj in T:
        out[ti+di][tj+dj] = 4
    return out