from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    top = []
    for row in reversed(grid):
        r = row[::-1]
        full = r + r[::-1]
        top.append(full)
    return top + top[::-1]