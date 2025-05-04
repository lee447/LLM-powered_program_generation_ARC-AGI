from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    colored_rows = [r for r in range(h) if any(cell not in (0,5) for cell in grid[r])]
    starts, lengths, patterns = [], [], []
    for r in colored_rows:
        cols = [c for c in range(w) if grid[r][c] not in (0,5)]
        cmin, cmax = min(cols), max(cols)
        starts.append(cmin)
        length = cmax - cmin + 1
        lengths.append(length)
        patterns.append([grid[r][c] for c in range(cmin, cmin + length)])
    n = len(starts)
    if n >= 2:
        d_s = starts[1] - starts[0]
        d_l = lengths[1] - lengths[0]
    else:
        d_s = d_l = 0
    next_start = starts[-1] + d_s
    next_length = lengths[-1] + d_l
    P0 = patterns[0] if patterns else []
    if P0:
        first = P0[0]
        if all(v == first for v in P0):
            pattern_next = [first] * next_length
        else:
            times = next_length // len(P0) + 1
            pattern_next = (P0 * times)[:next_length]
    else:
        pattern_next = [0] * next_length
    out = [[0] * w for _ in range(3)]
    for i, v in enumerate(pattern_next):
        pos = next_start + i
        if 0 <= pos < w:
            out[1][pos] = v
    return out