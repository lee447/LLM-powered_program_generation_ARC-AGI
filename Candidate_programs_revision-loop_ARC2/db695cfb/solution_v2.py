from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cnt = {}
    for r in grid:
        for c in r:
            cnt[c] = cnt.get(c, 0) + 1
    bg = max(cnt, key=lambda x: cnt[x])
    others = [c for c in cnt if c != bg]
    if len(others) == 0:
        return grid
    if len(others) == 1:
        c1 = others[0]
        c2 = None
    else:
        others.sort(key=lambda x: cnt[x])
        c1, c2 = others[0], others[1]
    pos1 = [(i,j) for i in range(h) for j in range(w) if grid[i][j] == c1]
    pos2 = [(i,j) for i in range(h) for j in range(w) if c2 is not None and grid[i][j] == c2]
    out = [row[:] for row in grid]
    if len(pos1) >= 2:
        p1, p2 = max(((a,b) for a in pos1 for b in pos1 if a!=b), key=lambda x: abs(x[0][0]-x[1][0])+abs(x[0][1]-x[1][1]))
        dr = (p2[0]-p1[0])//max(1,abs(p2[0]-p1[0]))
        dc = (p2[1]-p1[1])//max(1,abs(p2[1]-p1[1]))
        if abs(p2[0]-p1[0]) == abs(p2[1]-p1[1]):
            steps = abs(p2[0]-p1[0]) + 1
            for i in range(steps):
                r = p1[0] + dr*i
                c = p1[1] + dc*i
                if out[r][c] != c2:
                    out[r][c] = c1
    if c2 is not None:
        if len(pos1) >= 2:
            # line of c1: direction dr,dc through p1->p2
            for (r0,c0) in pos2:
                if (r0-p1[0])*dc == (c0-p1[1])*dr:
                    dr2, dc2 = -dc, dr
                    r, c = r0, c0
                    while 0 <= r < h and 0 <= c < w:
                        if out[r][c] == bg:
                            out[r][c] = c2
                        r += dr2; c += dc2
                    r, c = r0-dr2, c0-dc2
                    while 0 <= r < h and 0 <= c < w:
                        if out[r][c] == bg:
                            out[r][c] = c2
                        r -= dr2; c -= dc2
        else:
            for (r0,c0) in pos2:
                # try both diagonal directions
                for dr2,dc2 in ((1,1),(1,-1),(-1,1),(-1,-1)):
                    r, c = r0, c0
                    while 0 <= r < h and 0 <= c < w:
                        if out[r][c] == bg:
                            out[r][c] = c2
                        r += dr2; c += dc2
    return out