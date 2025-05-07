from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    nonz = [any(c != 0 for c in row) for row in grid]
    clusters = []
    i = 0
    while i < h:
        if nonz[i]:
            j = i
            while j < h and nonz[j]:
                j += 1
            clusters.append((i, j))
            i = j
        else:
            i += 1
    perfect = []
    segs = []
    for r0, r1 in clusters:
        row = grid[r0]
        c0 = None
        for c in range(w):
            if row[c] != 0:
                c0 = c
                break
        if c0 is None:
            perfect.append(False)
            segs.append(None)
            continue
        C = row[c0]
        c1 = c0
        while c1 < w and row[c1] == C:
            c1 += 1
        width = c1 - c0
        height = r1 - r0
        ok = True
        if width != height or width < 3:
            ok = False
        else:
            for c in range(c0, c1):
                if grid[r0][c] != C or grid[r1 - 1][c] != C:
                    ok = False
                    break
        if ok:
            for r in range(r0 + 1, r1 - 1):
                if grid[r][c0] != C or grid[r][c1 - 1] != C:
                    ok = False
                    break
                for c in range(c0 + 1, c1 - 1):
                    if grid[r][c] != 0:
                        ok = False
                        break
                if not ok:
                    break
        perfect.append(ok)
        segs.append((r0, r1, c0, c1, C) if ok else None)
    n = len(clusters)
    center = n // 2
    min_d = None
    for j, ok in enumerate(perfect):
        if ok:
            d = abs(j - center)
            if min_d is None or d < min_d:
                min_d = d
    out = [row[:] for row in grid]
    if min_d is not None:
        for j, s in enumerate(segs):
            if perfect[j] and abs(j - center) == min_d:
                r0, r1, c0, c1, C = s
                for r in range(r0 + 1, r1 - 1):
                    for c in range(c0 + 1, c1 - 1):
                        if (r + c) % 2 == 1:
                            out[r][c] = C
    return out