from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    groups = {}
    for r in range(R-1):
        for c in range(C-1):
            if grid[r][c] == 8 and grid[r][c+1] == 8 and grid[r+1][c] == 8 and grid[r+1][c+1] == 8:
                groups.setdefault(r, []).append(c)
    out = []
    for r in sorted(groups):
        cs = sorted(groups[r])
        c1, c2 = cs[0], cs[1]
        start, end = c1+2, c2-1
        out.append(grid[r][start:end+1])
        out.append(grid[r+1][start:end+1])
    return out