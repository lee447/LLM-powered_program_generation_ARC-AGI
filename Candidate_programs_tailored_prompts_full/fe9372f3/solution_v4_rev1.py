from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    res = [[0]*W for _ in range(H)]
    reds = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 2]
    for r, c in reds:
        res[r][c] = 2
    for r, c in reds:
        cnt = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == 2:
                cnt += 1
        if cnt == 4:
            cr, cc = r, c
            break
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        r, c = cr+dr, cc+dc
        while 0 <= r < H and 0 <= c < W:
            if res[r][c] == 0:
                res[r][c] = 1
            r += dr; c += dc
    pattern = [8, 8, 4]
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = cr+dr, cc+dc
        k = 1
        while 0 <= r < H and 0 <= c < W:
            if k > 1 and res[r][c] == 0:
                res[r][c] = pattern[(k-2) % 3]
            k += 1
            r += dr; c += dc
    return res