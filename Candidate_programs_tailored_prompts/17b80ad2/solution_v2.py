from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0]) if H else 0
    result = [row[:] for row in grid]
    anchors = [c for c in range(W) if any(grid[r][c] == 5 for r in range(H))]
    for c in anchors:
        last = {}
        for r in range(H):
            v = grid[r][c]
            if v != 0:
                if v not in last or r > last[v]:
                    last[v] = r
        segments = sorted((r, v) for v, r in last.items())
        prev = -1
        for r, v in segments:
            for rr in range(prev+1, r+1):
                result[rr][c] = v
            prev = r
    return result