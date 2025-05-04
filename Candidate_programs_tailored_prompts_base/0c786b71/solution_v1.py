from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    r = [row[::-1] for row in grid[::-1]]
    h = [row + row[::-1] for row in r]
    return h + h[::-1]