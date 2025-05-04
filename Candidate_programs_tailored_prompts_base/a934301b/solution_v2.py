from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    patches = []
    for i in range(h-2):
        for j in range(w-2):
            cnt8 = cnt1 = 0
            for di in range(3):
                for dj in range(3):
                    v = grid[i+di][j+dj]
                    if v == 8: cnt8 += 1
                    elif v == 1: cnt1 += 1
            if cnt8 == 1 and cnt1 == 8:
                patches.append((i, j))
    if not patches:
        return [[0]*w for _ in range(h)]
    bands = {}
    max_band = 0
    for i, j in patches:
        b = i // 3
        max_band = max(max_band, b)
        bands.setdefault(b, []).append((i, j))
    keep_bands = [b for b in bands if b < max_band]
    kept = []
    for b in keep_bands:
        row = max(bands[b], key=lambda x: x[1])
        kept.append(row)
    out = [[0]*w for _ in range(h)]
    for i, j in kept:
        for di in range(3):
            for dj in range(3):
                out[i+di][j+dj] = grid[i+di][j+dj]
    return out