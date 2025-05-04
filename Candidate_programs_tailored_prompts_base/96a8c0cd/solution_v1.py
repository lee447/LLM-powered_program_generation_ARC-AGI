from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    m = len(grid)
    n = len(grid[0]) if m>0 else 0
    out = [row[:] for row in grid]
    row_segs = {}
    for r in range(m):
        c = 0
        while c < n:
            if grid[r][c] != 0:
                color = grid[r][c]
                start = c
                while c+1 < n and grid[r][c+1] == color:
                    c += 1
                end = c
                length = end - start + 1
                if color == 2 or length >= 3:
                    row_segs.setdefault(r, []).append((start, end))
            c += 1
    col_segs = {}
    for c in range(n):
        r = 0
        while r < m:
            if grid[r][c] != 0:
                color = grid[r][c]
                start = r
                while r+1 < m and grid[r+1][c] == color:
                    r += 1
                end = r
                length = end - start + 1
                if color == 2 or length >= 3:
                    col_segs.setdefault(c, []).append((start, end))
            r += 1
    for r, segs in row_segs.items():
        if len(segs) < 2: continue
        segs.sort()
        for i in range(len(segs)-1):
            end1 = segs[i][1]
            start2 = segs[i+1][0]
            for c in range(end1+1, start2):
                out[r][c] = 2
    for c, segs in col_segs.items():
        if len(segs) < 2: continue
        segs.sort()
        for i in range(len(segs)-1):
            end1 = segs[i][1]
            start2 = segs[i+1][0]
            for r in range(end1+1, start2):
                out[r][c] = 2
    return out