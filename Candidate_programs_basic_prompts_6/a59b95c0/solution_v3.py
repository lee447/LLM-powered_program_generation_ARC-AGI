from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    k = len({v for row in grid for v in row})
    return [row * k for _ in range(k) for row in grid]