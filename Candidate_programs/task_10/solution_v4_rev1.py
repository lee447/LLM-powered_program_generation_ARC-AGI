from typing import List
import math
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    hrs = []
    for r in range(h):
        for c in range(w-1):
            if grid[r][c] != 0 and grid[r][c+1] == grid[r][c]:
                hrs.append(r)
                break
    if not hrs:
        return [row[:] for row in grid]
    r0, rN = min(hrs), max(hrs)
    def sft(r):
        if r == r0 or r == rN:
            return 0
        return int(-math.sin(math.pi/2 * ((r - r0) % 4)))
    out = [[0]*w for _ in range(h)]
    for r in range(h):
        s = sft(r)
        for c in range(w):
            v = grid[r][c]
            if v:
                nc = c + s
                if 0 <= nc < w:
                    out[r][nc] = v
    return out