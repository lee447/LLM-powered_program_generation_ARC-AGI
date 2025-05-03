from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    new = [row[::-1] + row for row in grid]
    return new[::-1] + new