from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    block = [row[::-1] + row for row in grid]
    return [block[h - 1 - i] for i in range(h)] + [block[i] for i in range(h)]