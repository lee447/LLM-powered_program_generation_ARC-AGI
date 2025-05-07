from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    N = len(grid)
    M = N // 2
    return [
        [grid[0][0], grid[1][1], grid[0][N-1]],
        [grid[1][N-2], grid[M][M], grid[N-2][1]],
        [grid[N-1][0], grid[N-2][N-2], grid[N-1][N-1]],
    ]