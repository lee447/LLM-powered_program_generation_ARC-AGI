from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    k = len({c for row in grid for c in row})
    return [row * k for row in grid for _ in range(k)]