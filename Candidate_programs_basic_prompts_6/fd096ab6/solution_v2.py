def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import defaultdict, deque
    cells = defaultdict(list)
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 1:
                cells[v].append((r, c))
    # find template color (max count)
    temp_col = max(cells, key=lambda c: len(cells[c]))
    P = set(cells[temp_col])
    # locate template center
    ctr = None
    for r, c in P:
        same_r = sum(1 for rr, cc in P if rr == r)
        same_c = sum(1 for rr, cc in P if cc == c)
        if same_r >= 2 and same_c >= 2:
            ctr = (r, c)
            break
    T = [(r - ctr[0], c - ctr[1]) for r, c in P if (r, c) != ctr]
    def rot(pt, k):
        r, c = pt
        if k == 1: return (-c, r)
        if k == 2: return (-r, -c)
        if k == 3: return (c, -r)
        return (r, c)
    out = [row[:] for row in grid]
    for col, pts in cells.items():
        if col == temp_col: continue
        Pset = set(pts)
        best = ( -1, None, None)
        for k in range(4):
            R = [rot(p, k) for p in T]
            for (r0, c0) in Pset:
                for q in R:
                    tr = r0 - q[0]; tc = c0 - q[1]
                    cnt = sum((tr + rr, tc + cc) in Pset for rr, cc in R)
                    if cnt > best[0]:
                        best = (cnt, k, (tr, tc))
        _, k, (tr, tc) = best
        R = [rot(p, k) for p in T]
        for dr, dc in R:
            r2, c2 = tr + dr, tc + dc
            if 0 <= r2 < h and 0 <= c2 < w:
                out[r2][c2] = col
    return out