from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    mapping = {8:2, 3:1, 5:4}
    vals = {c for row in grid for c in row}
    o = next(c for c in vals if c != 0)
    r = mapping[o]
    return [[0 if c == o else r for c in row] for row in grid]