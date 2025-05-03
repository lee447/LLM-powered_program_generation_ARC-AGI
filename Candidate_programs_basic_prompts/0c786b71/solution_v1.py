from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    tl = [row[::-1] for row in grid[::-1]]
    top = [r + r[::-1] for r in tl]
    return top + top[::-1]