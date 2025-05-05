def solve(grid):
    H, W = len(grid), len(grid[0])
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] != 0]
    rmin, rmax = min(r for r, c in pts), max(r for r, c in pts)
    cmin, cmax = min(c for r, c in pts), max(c for r, c in pts)
    sub = [[grid[r][c] for c in range(cmin, cmax+1)] for r in range(rmin, rmax+1)]
    h, w = len(sub), len(sub[0])
    def rot90(m):
        return [ [m[h-1-r][c] for r in range(len(m)) ] for c,mh in enumerate(m[0]) ]
    g0, g1 = sub, rot90(sub)
    g2 = [row[::-1] for row in g0[::-1]]
    g3 = [row[::-1] for row in g1[::-1]]
    h0, w0 = len(g0), len(g0[0])
    h1, w1 = len(g1), len(g1[0])
    h2, w2 = len(g2), len(g2[0])
    h3, w3 = len(g3), len(g3[0])
    top = max(h0, h3); bot = max(h2, h1)
    left = max(w3, w2); right = max(w0, w1)
    R = top + 1 + bot; C = left + 1 + right
    out = [[0]*C for _ in range(R)]
    def place(g, hh, ww, rr, cc):
        for i in range(hh):
            for j in range(ww):
                if g[i][j]:
                    out[rr+i][cc+j] = g[i][j]
    place(g0, h0, w0, (top-h0)//2, left+1 + (right-w0)//2)
    place(g1, h1, w1, top+1 + (bot-h1)//2, left+1 + (right-w1)//2)
    place(g2, h2, w2, top+1 + (bot-h2)//2, (left-w2)//2)
    place(g3, h3, w3, (top-h3)//2, (left-w3)//2)
    return out