from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    segs = []
    for j in range(w):
        i = 0
        while i < h - 2:
            E = grid[i][j]
            C = grid[i+1][j]
            if E != 0 and C != 0 and C != E:
                r = i + 2
                while r < h and grid[r][j] == C:
                    r += 1
                if r < h and grid[r][j] == E and r - i - 1 >= 1:
                    segs.append((j, i, r, C, E, r - i - 1))
                    i = r
                    continue
            i += 1
    if len(segs) == 2:
        _, i1, k1, C1, E1, L1 = segs[0]
        _, i2, k2, C2, E2, L2 = segs[1]
        pick = None
        odd1, odd2 = L1 % 2, L2 % 2
        if odd1 != odd2:
            pick = 0 if odd1 else 1
        elif odd1 == 1 and odd2 == 1:
            pick = 0 if L1 < L2 else 1
        else:
            pick = 0 if E1 < E2 else 1
        j, i, k, C, E, L = segs[pick]
        out = [row[:] for row in grid]
        for r in range(i+1, k):
            out[r][j] = E
        return out
    return [row[:] for row in grid]