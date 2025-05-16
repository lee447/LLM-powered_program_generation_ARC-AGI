from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    cnt = {}
    for r in grid:
        for v in r:
            cnt[v] = cnt.get(v, 0) + 1
    bg = max(cnt, key=cnt.get)
    best = None
    best_defects = None
    best_area = 0
    for c in cnt:
        if c == bg:
            continue
        for r1 in range(H):
            for r2 in range(r1 + 1, H):
                for c1 in range(W):
                    for c2 in range(c1 + 1, W):
                        perim = 2*((r2 - r1 + 1) + (c2 - c1 + 1)) - 4
                        defects = 0
                        for x in range(c1, c2 + 1):
                            if grid[r1][x] != c: defects += 1
                            if grid[r2][x] != c: defects += 1
                        for y in range(r1 + 1, r2):
                            if grid[y][c1] != c: defects += 1
                            if grid[y][c2] != c: defects += 1
                        area = (r2 - r1 + 1) * (c2 - c1 + 1)
                        if best is None or defects < best_defects or (defects == best_defects and area > best_area):
                            best = (r1, r2, c1, c2)
                            best_defects = defects
                            best_area = area
    if best is None:
        return grid
    r1, r2, c1, c2 = best
    return [row[c1:c2+1] for row in grid[r1:r2+1]]