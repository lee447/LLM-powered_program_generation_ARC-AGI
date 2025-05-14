from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    color = max(max(row) for row in grid)
    output = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == color:
                output[i * 3][j * 3] = color
                output[i * 3][j * 3 + 1] = color
                output[i * 3][j * 3 + 2] = color
                output[i * 3 + 1][j * 3] = color
                output[i * 3 + 1][j * 3 + 2] = color
                output[i * 3 + 2][j * 3] = color
                output[i * 3 + 2][j * 3 + 1] = color
                output[i * 3 + 2][j * 3 + 2] = color
    return output