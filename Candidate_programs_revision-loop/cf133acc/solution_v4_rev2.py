from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    hruns = {}
    for i in range(h):
        j = 0
        while j < w:
            c = grid[i][j]
            if c != 0:
                k = j + 1
                while k < w and grid[i][k] == c:
                    k += 1
                if k - j >= 3 and c not in hruns:
                    hruns[c] = i
                j = k
            else:
                j += 1
    vruns = {}
    for j in range(w):
        i = 0
        while i < h:
            c = grid[i][j]
            if c != 0:
                k = i + 1
                while k < h and grid[k][j] == c:
                    k += 1
                if k - i >= 3 and c not in vruns:
                    vruns[c] = (j, i, k - 1)
                i = k
            else:
                i += 1
    for c, H in sorted(hruns.items(), key=lambda x: x[1]):
        cols = [j for j in range(w) if grid[H][j] == c]
        hmin, hmax = min(cols), max(cols)
        for j in range(hmin, hmax + 1):
            out[H][j] = c
        pivot_h = None
        for j in range(hmin, hmax + 1):
            if grid[H][j] == 0:
                pivot_h = j
                break
        if c in vruns:
            vc, vmin, vmax = vruns[c]
            start = min(H, vmin) + 1
            end = max(H, vmin)
            for i in range(start, end):
                if grid[i][vc] == 0 and out[i][vc] == 0:
                    out[i][vc] = c
                else:
                    break
        else:
            if pivot_h is None:
                continue
            for i in range(H - 1, -1, -1):
                if grid[i][pivot_h] == 0 and out[i][pivot_h] == 0:
                    out[i][pivot_h] = c
                else:
                    break
    return out