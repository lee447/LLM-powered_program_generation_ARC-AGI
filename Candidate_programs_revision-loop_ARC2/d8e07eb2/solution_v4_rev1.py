from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg, fill = 8, 3
    bands = []
    r = 0
    while r < h:
        if any(grid[r][c] != bg for c in range(w)):
            start = r
            while r < h and any(grid[r][c] != bg for c in range(w)):
                r += 1
            bands.append((start, r - 1))
        else:
            r += 1
    band_info = []
    for i, (r0, r1) in enumerate(bands):
        has6 = any(grid[r][c] == 6 for r in range(r0, r1 + 1) for c in range(w))
        band_info.append((r0, r1, i % 2 == 0, not has6))
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == bg:
                for r0, r1, is_even, no6 in band_info:
                    if r0 - 1 <= r <= r1 + 1 and is_even:
                        if r == r0 - 1 or r == r1 + 1 or (r0 <= r <= r1 and no6):
                            out[r][c] = fill
                        break
    return out