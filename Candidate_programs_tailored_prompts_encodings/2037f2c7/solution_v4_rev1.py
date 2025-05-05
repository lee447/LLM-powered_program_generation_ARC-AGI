from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    stripes = []
    for r in range(h):
        runs = []
        c = 0
        while c < w:
            if grid[r][c] == 4:
                start = c
                while c < w and grid[r][c] == 4:
                    c += 1
                length = c - start
                if length >= 3:
                    runs.append((start, c - 1))
            else:
                c += 1
        for s, e in runs:
            stripes.append((r, s, e))
    stripes.sort()
    rows = [r for r,_,_ in stripes]
    segs = []
    for i in range(len(rows) - 1):
        segs.append((rows[i], rows[i+1]))
    if not segs:
        return []
    c0, c1 = min(s for _,s,_ in stripes), max(e for _,_,e in stripes)
    out = []
    for a, b in segs:
        y = a + 1
        if y > h - 1:
            y = b - 1
        row = []
        for x in range(c0, c1 + 1):
            row.append(8 if grid[y][x] != 0 else 0)
        out.append(row)
    return out