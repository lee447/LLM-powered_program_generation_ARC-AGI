def solve(grid):
    h = len(grid)
    w = len(grid[0])
    freq = {}
    for y in range(h):
        for x in range(w):
            freq[grid[y][x]] = freq.get(grid[y][x], 0) + 1
    bg = max(freq, key=lambda c: freq[c])
    tgt = next(c for c in freq if c != bg)
    best_row = None
    best_cnt = 0
    segs_by_row = {}
    for y in range(h):
        segs = []
        x = 0
        while x < w:
            if grid[y][x] == tgt:
                start = x
                while x < w and grid[y][x] == tgt:
                    x += 1
                segs.append((start, x-1))
            else:
                x += 1
        segs_by_row[y] = segs
        if len(segs) > best_cnt:
            best_cnt = len(segs)
            best_row = y
    if best_row is None or best_cnt < 2:
        return grid
    segs = segs_by_row[best_row]
    segs = sorted(segs, key=lambda s: s[0])
    lengths = [b-a+1 for a,b in segs]
    i_max = max(range(len(segs)), key=lambda i: lengths[i])
    a_max, b_max = segs[i_max]
    mid_max = a_max + b_max
    best_i = None
    best_dist = None
    for i,(a,b) in enumerate(segs):
        if i == i_max: continue
        mid = a + b
        dist = abs(mid - mid_max)
        if best_i is None or dist < best_dist or (dist == best_dist and mid > (segs[best_i][0] + segs[best_i][1])):
            best_i = i
            best_dist = dist
    a_i, b_i = segs[best_i]
    lo = min(b_max, b_i) + 1
    hi = max(a_max, a_i) - 1
    for x in range(lo, hi+1):
        grid[best_row][x] = tgt
    return grid