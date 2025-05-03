from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    if h == 0:
        return []
    folded = [row[::-1] + row for row in grid]
    result = []
    for i in range(h - 1, -1, -1):
        result.append(folded[i])
    for i in range(h):
        result.append(folded[i])
    return result