def solve(grid):
    H, W = len(grid), len(grid[0])
    subr, subc = H//3, W//3
    # find blueprint cell
    found = False
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 2:
                br, bc = i//subr, j//subc
                found = True
                break
        if found: break
    r0, c0 = br*subr, bc*subc
    # collect template window coords
    t4 = []
    t2 = []
    for i in range(r0, r0+subr):
        for j in range(c0, c0+subc):
            if grid[i][j] == 4:
                t4.append((i, j))
            if grid[i][j] == 2:
                t2.append((i, j))
    minr = min(r for r,c in t4+t2) - r0
    minc = min(c for r,c in t4+t2) - c0
    maxr = max(r for r,c in t4+t2) - r0
    maxc = max(c for r,c in t4+t2) - c0
    Ht, Wt = maxr-minr+1, maxc-minc+1
    T = [[0]*Wt for _ in range(Ht)]
    for r,c in t4:
        T[r-r0-minr][c-c0-minc] = 4
    for r,c in t2:
        T[r-r0-minr][c-c0-minc] = 2
    # generate symmetries
    def rotate(M):
        h, w = len(M), len(M[0])
        R = [[0]*h for _ in range(w)]
        for i in range(h):
            for j in range(w):
                R[j][h-1-i] = M[i][j]
        return R
    def flip(M):
        return [row[::-1] for row in M]
    mats = []
    M = T
    for _ in range(4):
        mats.append(M)
        mats.append(flip(M))
        M = rotate(M)
    out = [row[:] for row in grid]
    for M in mats:
        h, w = len(M), len(M[0])
        m4 = [(i,j) for i in range(h) for j in range(w) if M[i][j]==4]
        m2 = [(i,j) for i in range(h) for j in range(w) if M[i][j]==2]
        for i in range(H-h+1):
            for j in range(W-w+1):
                ok = True
                for di, dj in m4:
                    if grid[i+di][j+dj] != 4:
                        ok = False
                        break
                if not ok: continue
                for di, dj in m2:
                    if out[i+di][j+dj] == 0:
                        out[i+di][j+dj] = 2
    return out