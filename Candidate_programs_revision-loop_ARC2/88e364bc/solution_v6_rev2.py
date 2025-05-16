from typing import List
from collections import deque
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    new = [row[:] for row in grid]
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 4:
                continue
            best = -1
            best_dir = None
            best_v = None
            for di, dj in dirs:
                k = 1
                while True:
                    ni, nj = i + di*k, j + dj*k
                    if not (0 <= ni < h and 0 <= nj < w):
                        break
                    val = grid[ni][nj]
                    if val != 0 and val != 4:
                        zeros = k-1
                        if zeros > best:
                            best = zeros
                            best_dir = (di, dj)
                            best_v = val
                        break
                    k += 1
            if best_dir is None:
                continue
            di, dj = best_dir
            hi, hj = i + di*best, j + dj*best
            new[hi][hj] = 4
            new[i][j] = best_v
    return new