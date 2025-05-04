def solve(grid):
    h, w = len(grid), len(grid[0])
    top = next(r for r in range(h) if any(grid[r][c] != 0 for c in range(w)))
    bottom = h - 1 - next(r for r in range(h) if any(grid[h-1-r][c] != 0 for c in range(w)))
    left = next(c for c in range(w) if any(grid[r][c] != 0 for r in range(h)))
    right = w - 1 - next(c for c in range(w) if any(grid[r][w-1-c] != 0 for r in range(h)))
    H = bottom - top + 1
    W = right - left + 1
    h2, w2 = H // 2, W // 2
    P = [row[left:left+w2] for row in grid[top:top+h2]]
    orig = sorted({c for row in P for c in row})
    def transforms(mat):
        m, n = len(mat), len(mat[0])
        rot180 = [list(reversed(row)) for row in reversed(mat)]
        fx = [list(reversed(row)) for row in mat]
        fy = list(reversed(mat))
        return {"id": mat, "h": fx, "v": fy, "r": rot180}
    Ts = transforms(P)
    out = [row[:] for row in grid]
    for qi, (dr, dc) in enumerate(((0,0),(0,w2),(h2,0),(h2,w2))):
        quad = [row[left+dc:left+dc+w2] for row in grid[top+dr:top+dr+h2]]
        seeds = sorted({c for row in quad for c in row if c != 0})
        if qi == 0:
            T, mp = "id", {c: c for c in orig}
        else:
            if len(seeds) > 1:
                mp = {}
                ods = sorted(orig, reverse=True)
                for oc, sc in zip(ods, seeds):
                    mp[oc] = sc
                T = ["h","v","r"][qi-1]
            else:
                mp = {}
                mn, mx = min(orig), max(orig)
                s = seeds[0] if seeds else 0
                mp[mn] = 0
                mp[mx] = s
                T = "r"
        M = Ts[T]
        for i in range(h2):
            for j in range(w2):
                out[top+dr+i][left+dc+j] = mp.get(M[i][j], 0)
    return out