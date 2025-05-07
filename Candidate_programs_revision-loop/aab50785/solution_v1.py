from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = []
    i = 0
    while i < h - 1:
        pos = [j for j in range(w) if grid[i][j] == 8]
        if len(pos) == 4 and all(grid[i+1][j] == 8 for j in pos):
            pos.sort()
            left_end = pos[1]
            right_start = pos[2]
            for k in (i, i+1):
                res.append(grid[k][left_end+1:right_start])
            i += 2
        else:
            i += 1
    return res