from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] != 0]
    rmin, rmax = min(r for r, c in pts), max(r for r, c in pts)
    cmin, cmax = min(c for r, c in pts), max(c for r, c in pts)
    sub = [row[cmin:cmax+1] for row in grid[rmin:rmax+1]]
    def rot90(m):
        return [list(row) for row in zip(*m[::-1])]
    g0 = sub
    g1 = rot90(g0)
    g2 = rot90(g1)
    g3 = rot90(g2)
    h0, w0 = len(g0), len(g0[0])
    h1, w1 = len(g1), len(g1[0])
    h2, w2 = len(g2), len(g2[0])
    h3, w3 = len(g3), len(g3[0])
    top, bot = h3, h1
    left, right = w3, w1
    R, C = top + 1 + bot, left + 1 + right
    out = [[0]*C for _ in range(R)]
    def place(g, rr, cc):
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j] != 0:
                    out[rr+i][cc+j] = g[i][j]
    place(g3, 0, 0)
    place(g0, 0, left+1)
    place(g2, top+1, 0)
    place(g1, top+1, left+1)
    return out