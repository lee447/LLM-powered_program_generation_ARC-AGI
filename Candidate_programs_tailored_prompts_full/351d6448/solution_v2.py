from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    grey_rows = [r for r in range(rows) if all(grid[r][c] == 5 for c in range(cols))]
    clusters = []
    for r in sorted(grey_rows):
        if r > 0:
            rr = r - 1
            vals = [(c, grid[rr][c]) for c in range(cols) if grid[rr][c] not in (0,5)]
            if vals:
                cs = [c for c,_ in vals]
                start, end = min(cs), max(cs)
                pattern = [grid[rr][c] for c in range(start, end+1)]
                clusters.append((start, end, pattern))
    clusters.sort(key=lambda x: x[0])  # sort by start for ds,de; order of rows doesn't matter for deltas
    if len(clusters) < 2:
        return [[0]*cols for _ in range(3)]
    s0, e0, p0 = clusters[0]
    s1, e1, p1 = clusters[1]
    ds, de = s1 - s0, e1 - e0
    last_s, last_e, _ = clusters[-1]
    ps = last_s + ds
    pe = last_e + de
    use_pattern = all(len(p) == len(p0) and p == p0 for _,_,p in clusters)
    out = [[0]*cols for _ in range(3)]
    if use_pattern:
        for i, v in enumerate(p0):
            c = ps + i
            if 0 <= c < cols:
                out[1][c] = v
    else:
        v = clusters[-1][2][0]
        for c in range(ps, pe+1):
            if 0 <= c < cols:
                out[1][c] = v
    return out