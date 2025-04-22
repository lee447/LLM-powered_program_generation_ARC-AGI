from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    out = []
    for i in range(H):
        row = grid[H-1-i]
        out.append(row[::-1] + row)
    for i in range(H):
        out.append(out[H-1-i])
    return out