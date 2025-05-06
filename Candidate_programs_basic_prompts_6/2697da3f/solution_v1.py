def solve(grid):
    h, w = len(grid), len(grid[0])
    rmin, rmax = h, -1
    cmin, cmax = w, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0:
                if i < rmin: rmin = i
                if i > rmax: rmax = i
                if j < cmin: cmin = j
                if j > cmax: cmax = j
    ph = rmax - rmin + 1
    pw = cmax - cmin + 1
    P = [row[cmin:cmax+1] for row in grid[rmin:rmax+1]]
    N = max(ph, pw)
    tp = (N - ph + 1) // 2
    lp = (N - pw + 1) // 2
    Ppad = [[0]*N for _ in range(N)]
    for i in range(ph):
        for j in range(pw):
            Ppad[tp+i][lp+j] = P[i][j]
    B = [[0]*(3*N) for _ in range(3*N)]
    for bi, bj in [(0,1),(1,0),(1,2),(2,1)]:
        dr, dc = bi*N, bj*N
        for i in range(N):
            for j in range(N):
                v = Ppad[i][j]
                if v:
                    B[dr+i][dc+j] = v
    if N % 2 == 0:
        del B[N]
        for row in B:
            del row[N]
    return B