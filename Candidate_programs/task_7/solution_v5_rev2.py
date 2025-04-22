from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    row_seps = [i for i in range(h) if all(grid[i][j] == 4 for j in range(w))]
    col_seps = [j for j in range(w) if all(grid[i][j] == 4 for i in range(h))]
    rows = [-1] + row_seps + [h]
    cols = [-1] + col_seps + [w]
    bs = rows[1] - rows[0] - 1
    bH = len(rows) - 1
    bW = len(cols) - 1
    cnt = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v not in (0, 1, 4):
                cnt[v] = cnt.get(v, 0) + 1
    highlight = min(cnt.items(), key=lambda x: x[1])[0] if cnt else 0
    sum_main = 0
    m = min(bH, bW)
    for i in range(m):
        r0 = rows[i] + 1
        c0 = cols[i] + 1
        for dr in range(bs):
            for dc in range(bs):
                if grid[r0 + dr][c0 + dc] == 1:
                    sum_main += 1
    sum_anti = 0
    for i in range(bH):
        j = bW - 1 - i
        if 0 <= j < bW:
            r0 = rows[i] + 1
            c0 = cols[j] + 1
            for dr in range(bs):
                for dc in range(bs):
                    if grid[r0 + dr][c0 + dc] == 1:
                        sum_anti += 1
    use_main = sum_main >= sum_anti
    out = [row[:] for row in grid]
    for i in range(bH):
        j = i if use_main else bW - 1 - i
        if not (0 <= j < bW):
            continue
        r0 = rows[i] + 1
        c0 = cols[j] + 1
        for k in range(bs // 2 + 1):
            r1, c1 = r0 + k, c0 + k
            if 0 <= r1 < h and 0 <= c1 < w and grid[r1][c1] == 1:
                out[r1][c1] = highlight
            r2, c2 = r0 + k, c0 + (bs - 1 - k)
            if 0 <= r2 < h and 0 <= c2 < w and grid[r2][c2] == 1:
                out[r2][c2] = highlight
    return out