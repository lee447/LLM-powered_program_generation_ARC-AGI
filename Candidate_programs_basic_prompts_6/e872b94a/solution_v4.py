from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = min(len(grid), len(grid[0]))
    c = sum(1 for i in range(n) if grid[i][i] == 5)
    return [[0] for _ in range(c)]