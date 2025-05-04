from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    c = n // 2
    m = c + 1
    oc = m // 2
    out = [[0] * m for _ in range(m)]
    for i in range(n):
        for j in range(n):
            v = grid[i][j]
            if v == 0:
                continue
            dx = i - c
            dy = j - c
            if dx == 0 and dy == 0:
                dxp, dyp = 0, 0
            else:
                if abs(dx) == c:
                    dxp = dx // abs(dx)
                    dyp = dy // abs(dy)
                else:
                    if dx * dy > 0:
                        dxp = dx // abs(dx)
                        dyp = 0
                    else:
                        dxp = 0
                        dyp = dy // abs(dy)
            out[oc + dxp][oc + dyp] = v
    return out