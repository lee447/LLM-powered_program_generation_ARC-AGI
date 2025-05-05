from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    steps = []
    for c in range(w):
        cnt = sum(grid[r][c] == 2 for r in range(h))
        if cnt > 0:
            steps.append(2 if cnt > 1 else 1)
    steps = steps[:7]
    out = [[0] * 7 for _ in range(8)]
    out[0][3] = 3
    for i, s in enumerate(steps):
        for j in range(s):
            out[i + 1][3 + j] = 2
    return out