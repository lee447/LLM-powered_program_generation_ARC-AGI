from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    return [row[:] for row in grid]