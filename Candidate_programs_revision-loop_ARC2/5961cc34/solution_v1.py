from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    comp = {(r, c) for r in range(h) for c in range(w) if grid[r][c] in (1, 3)}
    res = [[8] * w for _ in range(h)]
    for r, c in comp:
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= h or nc < 0 or nc >= w or (nr, nc) not in comp:
                res[r][c] = 2
                break
    return res