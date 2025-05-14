from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    result = []
    for i in range(0, len(grid), 3):
        row = []
        for j in range(len(grid[0])):
            if j % 3 == 1:
                row.append(grid[i][j])
        result.append(row)
    return result