from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    out = []
    seq = list(reversed(grid)) + grid
    for row in seq:
        out.append(row[::-1] + row)
    return out