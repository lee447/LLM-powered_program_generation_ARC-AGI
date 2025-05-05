from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    rings = []
    for r in range(h - 4):
        for c in range(w - 4):
            ok = True
            for dr in range(5):
                for dc in range(5):
                    if dr in (0, 4) or dc in (0, 4):
                        if grid[r+dr][c+dc] != 3:
                            ok = False
                            break
                    else:
                        if grid[r+dr][c+dc] != 0:
                            ok = False
                            break
                if not ok:
                    break
            if ok:
                rings.append((r, c))
    rings.sort(key=lambda x: x[0])
    if len(rings) >= 2:
        r0, c0 = rings[0]
        for dr in range(5):
            for dc in range(5):
                res[r0+dr][c0+5+dc] = 1
        if len(rings) >= 3:
            r1, c1 = rings[1]
            r2, c2 = rings[2]
        else:
            r1, c1 = rings[0]
            r2, c2 = rings[1]
        top = r1 + 5 + ((r2 - (r1 + 5) - 3) // 2)
        left = c0 + 5 + ((5 - 3) // 2)
        for dr in range(3):
            for dc in range(3):
                if dr in (0, 2) or dc in (0, 2):
                    res[top+dr][left+dc] = 8
    return res