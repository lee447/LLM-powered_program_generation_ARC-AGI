from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    mirrored = [row[::-1] + row for row in grid]
    return mirrored[::-1] + mirrored