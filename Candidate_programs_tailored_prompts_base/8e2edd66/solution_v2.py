from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    out = [[0] * (n*n) for _ in range(n*n)]
    for bi in range(n):
        for bj in range(n):
            if grid[bi][bj] == 0:
                for di in range(n):
                    for dj in range(n):
                        if grid[di][dj] != 0:
                            out[bi*n + di][bj*n + dj] = grid[di][dj]
    return out