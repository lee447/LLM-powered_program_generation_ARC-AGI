from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    rows = [-1] + [i for i in range(h) if all(v == 4 for v in grid[i])] + [h]
    cols = [-1] + [j for j in range(w) if all(grid[i][j] == 4 for i in range(h))] + [w]
    bH, bW = len(rows) - 1, len(cols) - 1
    bs = rows[1] - rows[0] - 1
    cnt = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v not in (0, 1, 4):
                cnt[v] = cnt.get(v, 0) + 1
    highlight = min(cnt, key=cnt.get) if cnt else 0
    # measure which global diagonal has more 1's on its block-diagonal cells
    sum_main = sum(
        1
        for bi in range(bH)
        for k in range(bs)
        if rows[bi] + 1 + k < h and cols[bi] + 1 + k < w
        and bi < bW
        and bi == bi
        and grid[rows[bi] + 1 + k][cols[bi] + 1 + k] == 1
    )
    d_anti = bH // 2
    sum_anti = sum(
        1
        for bi in range(bH)
        for k in range(bs)
        if 0 <= d_anti - bi < bW
        and rows[bi] + 1 + k < h
        and cols[d_anti - bi] + 1 + (bs - 1 - k) < w
        and grid[rows[bi] + 1 + k][cols[d_anti - bi] + 1 + (bs - 1 - k)] == 1
    )
    use_main = sum_main >= sum_anti
    out = [row[:] for row in grid]
    for bi in range(bH):
        for bj in range(bW):
            if (use_main and bi == bj) or (not use_main and bi + bj == d_anti):
                r0, c0 = rows[bi] + 1, cols[bj] + 1
                for k in range((bs // 2) + 1):
                    if use_main:
                        r, c = r0 + k, c0 + k
                        if 0 <= r < h and 0 <= c < w and grid[r][c] == 1:
                            out[r][c] = highlight
                        r2, c2 = r0 + k, c0 + (bs - 1 - k)
                        if 0 <= r2 < h and 0 <= c2 < w and grid[r2][c2] == 1:
                            out[r2][c2] = highlight
                    else:
                        r, c = r0 + k, c0 + (bs - 1 - k)
                        if 0 <= r < h and 0 <= c < w and grid[r][c] == 1:
                            out[r][c] = highlight
                        r2, c2 = r0 + k, c0 + k
                        if 0 <= r2 < h and 0 <= c2 < w and grid[r2][c2] == 1:
                            out[r2][c2] = highlight
    return out