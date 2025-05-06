from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    twos = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    sr = sum(r for r, c in twos) // len(twos)
    sc = sum(c for r, c in twos) // len(twos)
    out = [row[:] for row in grid]
    pattern = [8, 8, 4]
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        cnt = 0
        k = 1
        while True:
            r, c = sr + dr * k, sc + dc * k
            if not (0 <= r < h and 0 <= c < w):
                break
            if grid[r][c] == 2:
                k += 1
                continue
            out[r][c] = pattern[cnt % 3]
            cnt += 1
            k += 1
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        k = 1
        while True:
            r, c = sr + dr * k, sc + dc * k
            if not (0 <= r < h and 0 <= c < w):
                break
            if out[r][c] != 2:
                out[r][c] = 1
            k += 1
    return out