from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    for c in {col for row in grid for col in row if col != 0}:
        H = []
        for i in range(h):
            j = 0
            while j < w:
                if grid[i][j] == c:
                    s = j
                    while j < w and grid[i][j] == c:
                        j += 1
                    e = j - 1
                    if e - s + 1 >= 2:
                        H.append((i, s, e))
                else:
                    j += 1
        V = []
        for j in range(w):
            i = 0
            while i < h:
                if grid[i][j] == c:
                    s = i
                    while i < h and grid[i][j] == c:
                        i += 1
                    e = i - 1
                    if e - s + 1 >= 2:
                        V.append((j, s, e))
                else:
                    i += 1
        # fill between two horizontals on same row
        from collections import defaultdict
        by_row = defaultdict(list)
        for i, s, e in H:
            by_row[i].append((s, e))
        for i, segs in by_row.items():
            segs.sort()
            for (s1, e1), (s2, e2) in zip(segs, segs[1:]):
                for x in range(e1+1, s2):
                    if res[i][x] == 0:
                        res[i][x] = c
        # fill between two verticals on same col
        by_col = defaultdict(list)
        for j, s, e in V:
            by_col[j].append((s, e))
        for j, segs in by_col.items():
            segs.sort()
            for (s1, e1), (s2, e2) in zip(segs, segs[1:]):
                for y in range(e1+1, s2):
                    if res[y][j] == 0:
                        res[y][j] = c
    return res