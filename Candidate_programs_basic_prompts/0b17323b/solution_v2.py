from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0]) if grid else 0
    ones = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]
    if len(ones) < 2:
        return [row[:] for row in grid]
    ones.sort()
    diff = ones[1][0] - ones[0][0]
    new = [row[:] for row in grid]
    r, c = ones[-1]
    while True:
        r, c = r + diff, c + diff
        if r < n and c < m:
            new[r][c] = 2
        else:
            break
    return new