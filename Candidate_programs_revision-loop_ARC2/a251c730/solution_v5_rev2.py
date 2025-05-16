from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    runs = {}
    for r in range(H):
        c = 0
        while c < W:
            v = grid[r][c]
            start = c
            while c + 1 < W and grid[r][c + 1] == v:
                c += 1
            end = c
            if end - start + 1 >= 3:
                runs.setdefault(v, []).append((r, start, end))
            c += 1
    best = None
    for v, segs in runs.items():
        for i in range(len(segs)):
            r1, c1, c2 = segs[i]
            for j in range(i + 1, len(segs)):
                r2, b1, b2 = segs[j]
                if r2 <= r1 + 1 or b1 != c1 or b2 != c2:
                    continue
                ok = True
                for r in range(r1, r2 + 1):
                    if grid[r][c1] != v or grid[r][c2] != v:
                        ok = False
                        break
                if not ok:
                    continue
                for rr in range(r1 + 1, r2):
                    for cc in range(c1 + 1, c2):
                        if grid[rr][cc] == v:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue
                area = (r2 - r1 + 1) * (c2 - c1 + 1)
                if best is None or area < best[0]:
                    best = (area, r1, r2, c1, c2)
    if best is None:
        return grid
    _, r1, r2, c1, c2 = best
    return [row[c1:c2+1] for row in grid[r1:r2+1]]