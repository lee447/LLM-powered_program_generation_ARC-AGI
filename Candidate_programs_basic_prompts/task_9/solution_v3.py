from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n_rows = len(grid)
    n_cols = len(grid[0])
    block_w = n_cols // 3
    res = [[0] * n_cols for _ in range(n_rows)]
    for b in range(3):
        cells = [(r, c) for r in range(n_rows) for c in range(b*block_w, (b+1)*block_w) if grid[r][c] == 5]
        cnt = len(cells)
        if cnt == 8:
            color = 3
        elif cnt == 1:
            color = 4
        elif cnt == block_w:
            rows = {r for r, _ in cells}
            if len(rows) == 1:
                r0 = next(iter(rows))
                color = 6 if r0 == 0 else 1
            else:
                color = 9
        elif cnt == 3:
            local = [(r, c - b*block_w) for r, c in cells]
            if all(cpr == block_w - 1 - r for r, cpr in local):
                color = 9
            else:
                r0 = local[0][0]
                color = 6 if r0 == 0 else 1
        else:
            color = 0
        for r in range(n_rows):
            for c in range(b*block_w, (b+1)*block_w):
                res[r][c] = color
    return res