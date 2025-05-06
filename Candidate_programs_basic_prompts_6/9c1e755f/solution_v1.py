from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    hsegs = []
    R = len(grid)
    C = len(grid[0])
    for r in range(R):
        c = 0
        while c < C:
            if grid[r][c] != 0:
                start = c
                while c + 1 < C and grid[r][c+1] != 0:
                    c += 1
                if c - start + 1 >= 2:
                    hsegs.append((r, start, c))
                c += 1
            else:
                c += 1
    groups = {}
    for (r, c1, c2) in hsegs:
        best_c = None
        best_len = -1
        for cand in (c1-1, c1):
            if 0 <= cand < C and grid[r][cand] != 0:
                cnt = 1
                i = r-1
                while i >= 0 and grid[i][cand] != 0:
                    cnt += 1
                    i -= 1
                i = r+1
                while i < R and grid[i][cand] != 0:
                    cnt += 1
                    i += 1
                if cnt > best_len:
                    best_len = cnt
                    best_c = cand
        if best_c is None:
            continue
        c = best_c
        sy = r
        while sy-1 >= 0 and grid[sy-1][c] != 0:
            sy -= 1
        ye = r
        while ye+1 < R and grid[ye+1][c] != 0:
            ye += 1
        key = (c, sy, ye)
        groups.setdefault(key, []).append((r, c1, c2))
    out = [row[:] for row in grid]
    for (c, sy, ye), H in groups.items():
        H.sort()
        L = len(H)
        for i in range(sy, ye+1):
            j = (i - sy) % L
            rH, c1, c2 = H[j]
            start = c1 + (1 if c1 == c else 0)
            for x in range(start, c2+1):
                out[i][x] = grid[rH][x]
    return out