from typing import List
from itertools import groupby

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for r in range(H):
        sixes = [c for c, v in enumerate(grid[r]) if v == 6]
        if not sixes:
            continue
        greens = [c for c, v in enumerate(grid[r]) if v == 3]
        for _, idxs in groupby(range(len(sixes)), key=lambda i: sixes[i] - i):
            block = [sixes[i] for i in idxs]
            s, e = block[0], block[-1]
            left = [c for c in greens if c < s]
            right = [c for c in greens if c > e]
            if not left or not right:
                continue
            L, R = max(left), min(right)
            arr = [grid[r][c] for c in range(L + 1, R) if grid[r][c] != 6]
            if len(arr) < len(block):
                continue
            for i, c in enumerate(block):
                out[r][c] = arr[-1 - i]
    return out