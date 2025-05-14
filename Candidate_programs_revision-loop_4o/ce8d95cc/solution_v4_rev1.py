from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    result = []
    for i in range(0, len(grid), 3):
        for j in range(3):
            result.append(grid[i + j])
    return result