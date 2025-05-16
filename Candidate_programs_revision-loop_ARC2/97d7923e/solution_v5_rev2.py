from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    segs = []
    for j in range(w):
        i = 0
        while i < h:
            c = grid[i][j]
            if c != 0:
                r = i + 1
                while r < h and grid[r][j] == c:
                    r += 1
                length = r - i
                if length > 1:
                    segs.append((j, i, length, c))
                i = r
            else:
                i += 1
    if not segs:
        return [row[:] for row in grid]
    odds = [s for s in segs if s[2] % 2 == 1]
    if len(odds) > 1:
        pick = max(odds, key=lambda x: x[2])
    else:
        evens = [s for s in segs if s[2] % 2 == 0]
        pick = min(evens, key=lambda x: x[2]) if evens else segs[0]
    j0, i0, L0, c0 = pick
    used = {v for row in grid for v in row}
    for fill in range(1, 10):
        if fill not in used:
            c1 = fill
            break
    out = [row[:] for row in grid]
    for r in range(i0 + 1, i0 + L0 - 1):
        out[r][j0] = c1
    return out