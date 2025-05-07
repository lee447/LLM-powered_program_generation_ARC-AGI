from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    pos = {}
    for r in range(h):
        cols = [c for c in range(w) if grid[r][c] == 4]
        if len(cols) == 2:
            key = (cols[0], cols[1])
            pos.setdefault(key, []).append(r)
    for (c1, c2), rows in pos.items():
        if len(rows) == 2:
            r1, r2 = sorted(rows)
            for y in range(r1 + 1, r2):
                for x in (c1, c2):
                    v = grid[y][x]
                    if v == 0: grid[y][x] = 8
                    elif v == 8: grid[y][x] = 0
                    elif v == 6: grid[y][x] = 7
                    elif v == 7: grid[y][x] = 6
    for (c1, c2), rows in pos.items():
        if len(rows) != 2:
            for r in rows:
                for x in range(min(c1, c2) + 1, max(c1, c2)):
                    v = grid[r][x]
                    if v == 0: grid[r][x] = 8
                    elif v == 8: grid[r][x] = 0
                    elif v == 6: grid[r][x] = 7
                    elif v == 7: grid[r][x] = 6
    return grid