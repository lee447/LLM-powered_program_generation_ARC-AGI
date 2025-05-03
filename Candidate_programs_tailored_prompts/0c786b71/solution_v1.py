def solve(grid):
    R, C = len(grid), len(grid[0])
    outR, outC = 2*R, 2*C
    O = [[0]*outC for _ in range(outR)]
    # mid indices in input
    if R % 2 == 1:
        mids = [R//2]
    else:
        mids = [R//2 - 1, R//2]
    if C % 2 == 1:
        midc = [C//2]
    else:
        midc = [C//2 - 1, C//2]
    # central rectangle in output
    central_rows = [i*2 + d for i in mids for d in (0,1)]
    central_cols = [j*2 + d for j in midc for d in (0,1)]
    # fill central rectangle from middle input row & col
    mrow = mids[-1]
    for j_idx, j in enumerate(midc):
        for d in (0,1):
            for r in central_rows:
                O[r][2*j + d] = grid[mrow][j]
    # extract Q from input
    # size Qh x Qw
    Qh = mids[-1] + 1
    Qw = len(midc)
    Q = [[0]*Qw for _ in range(Qh)]
    for a in range(Qh):
        ir = mids[-1] + 1 - a
        for b in range(Qw):
            ic = midc[-1] + 1 - b
            Q[a][b] = grid[ir][ic]
    # corners
    rl, rh = 0, outR - Qh
    cl, ch = 0, outC - Qw
    # TL
    for a in range(Qh):
        for b in range(Qw):
            O[rl + a][cl + b] = Q[a][b]
    # TR
    for a in range(Qh):
        for b in range(Qw):
            O[rl + a][ch + b] = Q[a][Qw - 1 - b]
    # BL
    for a in range(Qh):
        for b in range(Qw):
            O[rh + a][cl + b] = Q[Qh - 1 - a][b]
    # BR
    for a in range(Qh):
        for b in range(Qw):
            O[rh + a][ch + b] = Q[Qh - 1 - a][Qw - 1 - b]
    return O