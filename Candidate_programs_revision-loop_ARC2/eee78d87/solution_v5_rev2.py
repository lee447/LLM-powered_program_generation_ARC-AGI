from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    pts = [(i, j) for i in range(n) for j in range(n) if grid[i][j] not in (0, 7)]
    c = grid[pts[0][0]][pts[0][1]]
    is_x = False
    for i, j in pts:
        if sum((i+di, j+dj) in pts for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1))) == 4:
            is_x = False
            break
        if sum((i+di, j+dj) in pts for di, dj in ((1, 1), (1, -1), (-1, 1), (-1, -1))) == 4:
            is_x = True
            break
    m = n - 2
    R = m * m
    out = [[0] * R for _ in range(R)]
    def interior(x): return 1 <= x < m - 1
    mask_diag = [[(i == j or i + j == m - 1) and interior(i) and interior(j) for j in range(m)] for i in range(m)]
    mask_sq = [[interior(i) and interior(j) for j in range(m)] for i in range(m)]
    if is_x:
        mask0, mask1 = mask_diag, mask_sq
    else:
        mask0, mask1 = mask_sq, mask_diag
    inner = [row[1:-1] for row in grid[1:-1]]
    for bi in range(m):
        for bj in range(m):
            mask = mask0 if (bi + bj) % 2 == 0 else mask1
            col = inner[bi][bj]
            if col == 7:
                pat, bg = 7, 0
            else:
                pat, bg = 9, 7
            for di in range(m):
                for dj in range(m):
                    out[bi*m+di][bj*m+dj] = pat if mask[di][dj] else bg
    return out