from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    rs = [r for r in range(rows) for c in range(cols) if grid[r][c] == 2]
    cs = [c for r in range(rows) for c in range(cols) if grid[r][c] == 2]
    min_r, max_r, min_c, max_c = min(rs), max(rs), min(cs), max(cs)
    cr, cc = (min_r + max_r) // 2, (min_c + max_c) // 2
    out = [row[:] for row in grid]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                dr, dc = r - cr, c - cc
                adr, adc = abs(dr), abs(dc)
                if adr == adc:
                    out[r][c] = 1
                elif r == cr or c == cc:
                    rad = adr + adc
                    if rad >= 2:
                        out[r][c] = 4 if (rad - 2) % 3 == 2 else 8
    return out