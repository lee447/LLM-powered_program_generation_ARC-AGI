from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    top = []
    for row in grid[::-1]:
        row_rev = row[::-1]
        top.append(row_rev + row_rev[::-1])
    return top + top[::-1]