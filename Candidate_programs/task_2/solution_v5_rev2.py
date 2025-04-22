from typing import List
import math

def solve(grid: List[List[int]]) -> List[List[int]]:
    h0 = len(grid)
    w0 = len(grid[0]) if h0 else 0
    r0, r1 = h0, -1
    c0, c1 = w0, -1
    for i in range(h0):
        for j in range(w0):
            if grid[i][j] == 8:
                if i < r0: r0 = i
                if i > r1: r1 = i
                if j < c0: c0 = j
                if j > c1: c1 = j
    h = r1 - r0 + 1
    w = c1 - c0 + 1
    kmin = math.ceil(-r0 / h)
    kmax = math.floor((h0 - h - r0) / h)
    mmin = math.ceil(-c0 / w)
    mmax = math.floor((w0 - w - c0) / w)
    for k in range(kmin, kmax + 1):
        for m in range(mmin, mmax + 1):
            i = r0 + k * h
            j = c0 + m * w
            if i == r0 and j == c0: continue
            if 0 <= i and i + h <= h0 and 0 <= j and j + w <= w0:
                block = [row[j:j+w] for row in grid[i:i+h]]
                if all(cell != 8 for row in block for cell in row):
                    return block