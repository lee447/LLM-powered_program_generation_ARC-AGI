from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    cnt = {}
    for r in grid:
        for v in r:
            cnt[v] = cnt.get(v, 0) + 1
    bg = max(cnt, key=cnt.get)
    best_area = 0
    best_rect = None
    for c in cnt:
        if c == bg:
            continue
        for r1 in range(H):
            for r2 in range(r1 + 2, H):
                for c1 in range(W):
                    for c2 in range(c1 + 2, W):
                        area = (r2 - r1 + 1) * (c2 - c1 + 1)
                        if area <= best_area:
                            continue
                        ok = True
                        for x in range(c1, c2 + 1):
                            if grid[r1][x] != c or grid[r2][x] != c:
                                ok = False
                                break
                        if not ok:
                            continue
                        for y in range(r1 + 1, r2):
                            if grid[y][c1] != c or grid[y][c2] != c:
                                ok = False
                                break
                        if not ok:
                            continue
                        best_area = area
                        best_rect = (r1, r2, c1, c2)
    if best_rect is None:
        return grid
    r1, r2, c1, c2 = best_rect
    return [row[c1:c2+1] for row in grid[r1:r2+1]]