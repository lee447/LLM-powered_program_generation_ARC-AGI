from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    clusters = []
    for rr in range(rows):
        vals = [(c, grid[rr][c]) for c in range(cols) if grid[rr][c] not in (0, 5)]
        if vals:
            cs = [c for c, _ in vals]
            start, end = min(cs), max(cs)
            pattern = [grid[rr][c] for c in range(start, end + 1)]
            clusters.append((rr, start, end, pattern))
    if len(clusters) < 2:
        return [[0] * cols for _ in range(3)]
    clusters.sort(key=lambda x: x[0])
    starts = [s for _, s, _, _ in clusters]
    ends = [e for _, _, e, _ in clusters]
    ds = starts[1] - starts[0]
    de = ends[1] - ends[0]
    last_s, last_e = starts[-1], ends[-1]
    new_s, new_e = last_s + ds, last_e + de
    p0 = clusters[0][3]
    use_pattern = all(len(p) == len(p0) and p == p0 for _, _, _, p in clusters)
    out = [[0] * cols for _ in range(3)]
    if use_pattern:
        for i, v in enumerate(p0):
            c = new_s + i
            if 0 <= c < cols:
                out[1][c] = v
    else:
        v = clusters[-1][3][0]
        for c in range(new_s, new_e + 1):
            if 0 <= c < cols:
                out[1][c] = v
    return out