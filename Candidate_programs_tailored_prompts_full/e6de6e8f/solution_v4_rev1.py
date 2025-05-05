from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    steps = []
    for x in range(w):
        c = (grid[0][x] == 2) + (grid[1][x] == 2)
        if c:
            steps.append(c)
    steps = steps[:7]
    H, W = 8, 7
    out = [[0]*W for _ in range(H)]
    out[0][W//2] = 3
    x = W//2 - (steps[0] == 1)
    for r, s in enumerate(steps, start=1):
        if s == 2:
            out[r][x] = out[r][x+1] = 2
        else:
            out[r][x] = 2
        if r < H-1 and steps[r] == 2 and steps[r-1] == 2:
            x = min(x+1, W-1)
    return out