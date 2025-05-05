from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    out = []
    for row in reversed(grid):
        newrow = row[::-1] + row
        out.append(newrow)
        out.append(newrow)
    return out