from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg, fill = 8, 3
    bands = []
    r = 0
    while r < h:
        if any(grid[r][c] != bg for c in range(w)):
            r0 = r
            while r < h and any(grid[r][c] != bg for c in range(w)):
                r += 1
            bands.append((r0, r - 1))
        else:
            r += 1
    band_info = []
    for i, (r0, r1) in enumerate(bands):
        has6 = any(grid[r][c] == 6 for r in range(r0, r1+1) for c in range(w))
        cols = [c for r in range(r0, r1+1) for c in range(w) if grid[r][c] != bg]
        min_c, max_c = min(cols), max(cols)
        band_info.append((i, r0, r1, has6, min_c, max_c))
    out = [row[:] for row in grid]
    last = len(band_info) - 1
    for i, r0, r1, has6, min_c, max_c in band_info:
        if not has6 and i % 3 == 0:
            r_start, r_end = r0 - 1, r1 + 1
            for rr in range(r_start, r_end + 1):
                if rr < 0 or rr >= h:
                    continue
                if i == 0 or i == last:
                    c_lo, c_hi = 0, w - 1
                else:
                    c_lo, c_hi = min_c - 1, max_c + 1
                c_lo = max(0, c_lo)
                c_hi = min(w - 1, c_hi)
                for cc in range(c_lo, c_hi + 1):
                    if out[rr][cc] == bg:
                        out[rr][cc] = fill
    return out