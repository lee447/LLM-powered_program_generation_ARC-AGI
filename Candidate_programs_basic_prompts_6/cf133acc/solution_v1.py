from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    shapes = []
    for r in range(h):
        row = grid[r]
        colors = set(x for x in row if x != 0)
        for X in colors:
            pos = [j for j in range(w) if row[j] == X]
            if len(pos) < 2: continue
            segs = []
            i = 0
            while i < len(pos):
                s = pos[i]
                e = s
                while i + 1 < len(pos) and pos[i+1] == pos[i] + 1:
                    i += 1
                    e = pos[i]
                segs.append((s, e))
                i += 1
            if len(segs) == 2:
                s0, e0 = segs[0]
                s1, e1 = segs[1]
                if e0 + 2 == s1:
                    c = e0 + 1
                    if grid[r][c] == 0:
                        shapes.append((r, c, s0, e1, X))
    shapes.sort()
    for r, c, left, right, X in shapes:
        for j in range(left, right+1):
            out[r][j] = X
        for i in range(r-1, -1, -1):
            if out[i][c] != 0:
                break
            out[i][c] = X
    return out