from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    nonz = [any(c != 0 for c in row) for row in grid]
    clusters = []
    i = 0
    while i < h:
        if nonz[i]:
            j = i
            while j < h and nonz[j]:
                j += 1
            clusters.append(i)
            i = j
        else:
            i += 1
    for cr in clusters[1:]:
        row0 = grid[cr]
        segs = []
        c = 0
        while c < w:
            if row0[c] != 0:
                color = row0[c]
                start = c
                while c < w and row0[c] == color:
                    c += 1
                segs.append((start, c, color))
            else:
                c += 1
        for start, end, color in segs:
            ok = True
            for r in range(cr+1, cr+4):
                for cc in range(start+1, end-1):
                    if grid[r][cc] != 0:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            for r in range(cr+1, cr+4):
                for cc in range(start+1, end-1):
                    if grid[r][cc] == 0 and (r+cc) % 2 == 1:
                        out[r][cc] = color
    return out