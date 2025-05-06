def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import Counter, defaultdict, deque
    cnt = Counter()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0:
                cnt[grid[r][c]] += 1
    base = max((col for col in cnt if cnt[col] > 1), key=lambda c: cnt[c])
    insts = [(r,c,col) for r in range(h) for c in range(w)
             for col in [grid[r][c]] if col != 0 and col != base]
    base_coords = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==base]
    # pick pivot = the one in base with maximum neighbor count
    neigh = {}
    for r,c in base_coords:
        n=0
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            rr,cc=r+dr,c+dc
            if 0<=rr<h and 0<=cc<w and grid[rr][cc]==base: n+=1
        neigh[(r,c)] = n
    pivot = max(base_coords, key=lambda rc: neigh[rc])
    pr,pc = pivot
    out = [row[:] for row in grid]
    for tr,tc,col in insts:
        fh = -1 if tc>pc else 1
        fv = -1 if tr>pr else 1
        for r,c in base_coords:
            nr = tr + fv*(r-pr)
            nc = tc + fh*(c-pc)
            if 0<=nr<h and 0<=nc<w:
                out[nr][nc] = col
    return out