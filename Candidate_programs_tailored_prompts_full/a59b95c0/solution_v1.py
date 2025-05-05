from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    colors = {grid[i][j] for i in range(h) for j in range(w) if grid[i][j] != 0}
    f = len(colors)
    return [[grid[i % h][j % w] for j in range(w * f)] for i in range(h * f)]