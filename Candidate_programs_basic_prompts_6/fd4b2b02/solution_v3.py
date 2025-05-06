def solve(grid):
    R, C = len(grid), len(grid[0])
    pts = [(r, c) for r in range(R) for c in range(C) if grid[r][c] != 0]
    minr = min(r for r, c in pts)
    maxr = max(r for r, c in pts)
    minc = min(c for r, c in pts)
    maxc = max(c for r, c in pts)
    h = maxr - minr + 1
    w = maxc - minc + 1
    Ccol = grid[minr][minc]
    Dcol = 3 if Ccol != 3 else 6
    L = max(h, w)
    H = min(h, w)
    seglen = [L - 1] + [L] * 6 + [L - 1]
    segori = ['v', 'h', 'v', 'h', 'v', 'h', 'v', 'h']
    orig_ori = 'v' if h >= w else 'h'
    segcol = [(Ccol if o == orig_ori else Dcol) for o in segori]
    res = [[0] * C for _ in range(R)]
    # compute start so that original block is at (minr,minc)
    # we find the offset at which seg 2 produces the original
    # start by trial: we know seg2 start at (minr, minc) - dr2*H - dr1*(seglen[1]-1) - dr0*H
    # we reverse compute base
    def dirv(i):
        if segori[i] == 'v':
            return (1, 0)
        else:
            return (0, 1) if i % 4 in (1, 5) else (0, -1)
    # reverse simulate three segments to find start
    r2, c2 = minr, minc
    # go back from seg2 start over seg1 and seg0
    # seg2 start = end1 + d1 + d2*H
    d1 = dirv(1)
    d2 = dirv(2)
    end1_r = r2 - d1[0] - d2[0] * H
    end1_c = c2 - d1[1] - d2[1] * H
    # end1 = start1 + d1*(seglen[1]-1)
    d1 = dirv(1)
    start1_r = end1_r - d1[0] * (seglen[1] - 1)
    start1_c = end1_c - d1[1] * (seglen[1] - 1)
    # start1 = end0 + d0 + d1*H
    d0 = dirv(0)
    d1 = dirv(1)
    end0_r = start1_r - d0[0] - d1[0] * H
    end0_c = start1_c - d0[1] - d1[1] * H
    # end0 = start0 + d0*(seglen[0]-1)
    start0_r = end0_r - d0[0] * (seglen[0] - 1)
    start0_c = end0_c - d0[1] * (seglen[0] - 1)
    r, c = start0_r, start0_c
    for i in range(8):
        ori = segori[i]
        dl = seglen[i]
        col = segcol[i]
        dr, dc = dirv(i)
        for k in range(dl):
            br, bc = r + dr * k, c + dc * k
            if ori == 'v':
                for t in range(H):
                    res[br][bc + t] = col
            else:
                for t in range(H):
                    res[br + t][bc] = col
        end_r = r + dr * (dl - 1)
        end_c = c + dc * (dl - 1)
        if i < 7:
            dr2, dc2 = dirv(i + 1)
            r = end_r + dr + dr2 * H
            c = end_c + dc + dc2 * H
    return res