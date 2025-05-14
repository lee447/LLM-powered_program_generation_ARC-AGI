from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    return [[0] for _ in range(len(grid) - len(grid) // 3)]