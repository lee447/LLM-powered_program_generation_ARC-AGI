from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    top = []
    for row in grid[::-1]:
        top.append(row[::-1] + row[:])
    return top + top[::-1]