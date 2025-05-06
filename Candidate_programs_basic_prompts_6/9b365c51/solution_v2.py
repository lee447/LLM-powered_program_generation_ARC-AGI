from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    stripe_cols = []
    for c in range(w):
        vals = {grid[r][c] for r in range(h)}
        if len(vals) == 1:
            v = vals.pop()
            if v != 0:
                stripe_cols.append(c)
    stripe_cols.sort()
    stripe_colors = [grid[0][c] for c in stripe_cols]
    all_vals = {grid[r][c] for r in range(h) for c in range(w)}
    block_vals = all_vals - {0} - set(stripe_colors)
    block_color = block_vals.pop() if block_vals else None
    min_c = w
    max_c = -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] == block_color:
                if c < min_c: min_c = c
                if c > max_c: max_c = c
    if min_c > max_c:
        return [[0]*w for _ in range(h)]
    k = len(stripe_cols)
    width = max_c - min_c + 1
    base = width // k
    rem = width % k
    left_extra = rem // 2
    right_extra = rem - left_extra
    segs = []
    start = min_c
    for i in range(k):
        if i == 0:
            sz = base + left_extra
        elif i == k-1:
            sz = base + right_extra
        else:
            sz = base
        segs.append((start, start + sz - 1))
        start += sz
    out = [[0]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == block_color:
                for i,(a,b) in enumerate(segs):
                    if a <= c <= b:
                        out[r][c] = stripe_colors[i]
                        break
    return out