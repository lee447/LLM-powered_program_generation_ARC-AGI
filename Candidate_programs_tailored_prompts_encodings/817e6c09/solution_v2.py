from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    anchors = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c] == grid[r][c+1] == grid[r+1][c] == grid[r+1][c+1] == 2:
                anchors.append((r, c))
    anchors.sort(key=lambda x: x[1], reverse=True)
    out = [row[:] for row in grid]
    for i, (r, c) in enumerate(anchors):
        if i % 2 == 0:
            out[r][c] = out[r][c+1] = out[r+1][c] = out[r+1][c+1] = 8
    return out