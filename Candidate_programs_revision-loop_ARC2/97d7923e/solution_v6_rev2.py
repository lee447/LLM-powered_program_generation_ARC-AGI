from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    segments = []
    for j in range(w):
        i = 0
        best = None
        while i < h:
            if grid[i][j] != 0:
                c = grid[i][j]
                start = i
                i += 1
                while i < h and grid[i][j] == c:
                    i += 1
                end = i - 1
                length = end - start + 1
                if length >= 2 and (best is None or length > best[0]):
                    best = (length, j, start, end)
            else:
                i += 1
        if best:
            segments.append(best)
    if not segments:
        return grid
    cols = sorted(seg[1] for seg in segments)
    diffs = [cols[i+1] - cols[i] for i in range(len(cols)-1)]
    if not diffs:
        return grid
    md = min(diffs)
    cand = set()
    for i in range(len(cols)-1):
        if cols[i+1] - cols[i] == md:
            cand.add(cols[i])
            cand.add(cols[i+1])
    if not cand:
        return grid
    cand = sorted(cand)
    if len(cand) == 2:
        a, b = cand
        sa = next(s for s in segments if s[1] == a)[2]
        sb = next(s for s in segments if s[1] == b)[2]
        cand = [b if sa < sb else a]
    else:
        cand = cand[1:]
    maxc = max(c for row in grid for c in row)
    fill = maxc + 1 if maxc < 9 else 9
    for j in cand:
        _, _, st, ed = next(s for s in segments if s[1] == j)
        for i in range(st+1, ed):
            grid[i][j] = fill
    return grid