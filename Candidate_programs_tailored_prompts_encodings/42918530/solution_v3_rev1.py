from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    rows = []
    inside = False
    for i in range(H):
        if any(grid[i][j] != 0 for j in range(W)):
            if not inside:
                inside = True
                r0 = i
        else:
            if inside:
                rows.append((r0, i - 1))
                inside = False
    if inside:
        rows.append((r0, H - 1))
    cols = []
    inside = False
    for j in range(W):
        if any(grid[i][j] != 0 for i in range(H)):
            if not inside:
                inside = True
                c0 = j
        else:
            if inside:
                cols.append((c0, j - 1))
                inside = False
    if inside:
        cols.append((c0, W - 1))
    res = [row[:] for row in grid]
    top_r0, top_r1 = rows[0]
    for c0, c1 in cols:
        mask = [
            [1 if grid[i][j] != 0 else 0 for j in range(c0 + 1, c1)]
            for i in range(top_r0 + 1, top_r1)
        ]
        for br0, br1 in rows[1:]:
            color = next(grid[br0][j] for j in range(c0, c1 + 1) if grid[br0][j] != 0)
            for di in range(len(mask)):
                for dj in range(len(mask[0])):
                    if mask[di][dj]:
                        res[br0 + 1 + di][c0 + 1 + dj] = color
    return res