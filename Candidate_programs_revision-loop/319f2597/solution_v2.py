from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    rr = cc = None
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j] == 0 and grid[i][j+1] == 0 and grid[i+1][j] == 0 and grid[i+1][j+1] == 0:
                rr, cc = i, j
                break
        if rr is not None:
            break
    out = []
    for i in range(h):
        row = []
        for j in range(w):
            v = grid[i][j]
            if i == rr or i == rr+1 or j == cc or j == cc+1:
                row.append(v if v == 2 else 0)
            else:
                row.append(v)
        out.append(row)
    return out