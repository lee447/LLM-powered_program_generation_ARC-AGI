from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    targets = [j for j in range(w) if grid[h-1][j] != 0]
    for j in targets:
        positions = [i for i in range(h) if grid[i][j] != 0]
        values = [grid[i][j] for i in positions]
        for seg, r in enumerate(positions):
            start = positions[seg-1] + 1 if seg > 0 else 0
            end = r
            v = values[seg]
            for i in range(start, end + 1):
                out[i][j] = v
    return out