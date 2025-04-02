from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R = len(grid)
    C = len(grid[0]) if R else 0
    H = [row[::-1] for row in grid]
    V = grid[::-1]
    D = [row[::-1] for row in V]
    top = [D[i] + V[i] for i in range(R)]
    bottom = [H[i] + grid[i] for i in range(R)]
    return top + bottom