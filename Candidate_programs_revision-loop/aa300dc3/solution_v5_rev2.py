import numpy as np
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    zeros = {(r, c) for r in range(h) for c in range(w) if grid[r][c] == 0}
    best_chain = []
    for dr, dc in [(1, 1), (1, -1)]:
        for r, c in zeros:
            if (r - dr, c - dc) in zeros:
                continue
            chain = []
            rr, cc = r, c
            while (rr, cc) in zeros:
                chain.append((rr, cc))
                rr += dr
                cc += dc
            if len(chain) > len(best_chain):
                best_chain = chain
    out = [row[:] for row in grid]
    for r, c in best_chain:
        out[r][c] = 8
    return out