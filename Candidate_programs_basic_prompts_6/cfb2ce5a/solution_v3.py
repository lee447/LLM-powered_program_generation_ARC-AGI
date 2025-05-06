from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h0 = len(grid)
    w0 = len(grid[0])
    # find pattern colors (two most frequent non-zero)
    freq = {}
    for i in range(h0):
        for j in range(w0):
            v = grid[i][j]
            if v != 0:
                freq[v] = freq.get(v, 0) + 1
    pcs = sorted([c for c in freq if freq[c] > 0], key=lambda c: -freq[c])[:2]
    p0, p1 = pcs[0], pcs[1]
    # bounding box of pattern
    r0, r1 = h0, -1
    c0, c1 = w0, -1
    for i in range(h0):
        for j in range(w0):
            if grid[i][j] == p0 or grid[i][j] == p1:
                r0 = min(r0, i); r1 = max(r1, i)
                c0 = min(c0, j); c1 = max(c1, j)
    ph = r1 - r0 + 1
    pw = c1 - c0 + 1
    # extract pattern
    pat = [row[c0:c1+1] for row in grid[r0:r0+ph]]
    # rotations
    def rot_cw(m):
        H = len(m); W = len(m[0])
        return [[m[H-1-j][i] for j in range(H)] for i in range(W)]
    def rot_ccw(m):
        H = len(m); W = len(m[0])
        return [[m[j][W-1-i] for j in range(H)] for i in range(W)]
    def rot_180(m):
        return [row[::-1] for row in m[::-1]]
    pat_tr = rot_cw(pat)
    pat_bl = rot_ccw(pat)
    pat_br = rot_180(pat)
    # init output
    out = [[0]*w0 for _ in range(h0)]
    # fill TL
    for i in range(ph):
        for j in range(pw):
            out[r0+i][c0+j] = pat[i][j]
    # helper to find nearest seed
    def nearest(seeds, cr, cc):
        best = None
        bd = None
        bcd = None
        brd = None
        for (i,j,v) in seeds:
            d = abs(i-cr)+abs(j-cc)
            cd = abs(j-cc)
            rd = abs(i-cr)
            if bd is None or (d<bd or (d==bd and (cd<bcd or (cd==bcd and rd<brd)))):
                bd = d; bcd = cd; brd = rd; best = v
        return best if best is not None else 0
    # regionTR
    seeds_tr = [(i,j,grid[i][j]) for i in range(r0, r0+ph) for j in range(c1+1, c1+1+pw)
                if grid[i][j] not in (0,p0,p1)]
    seedTR = nearest(seeds_tr, r0, c1+pw)
    seedBL = nearest(seeds_tr, r1, c1+1)
    mp = {p0: seedTR, p1: seedBL}
    for i in range(ph):
        for j in range(pw):
            out[r0+i][c1+1+j] = mp.get(pat_tr[i][j], 0)
    # regionBL
    seeds_bl = [(i,j,grid[i][j]) for i in range(r1+1, r1+1+ph) for j in range(c0, c0+pw)
                if grid[i][j] not in (0,p0,p1)]
    seedTR2 = nearest(seeds_bl, r1+1, c1)
    seedBL2 = nearest(seeds_bl, r1+ph, c0)
    mp2 = {p0: seedTR2, p1: seedBL2}
    for i in range(ph):
        for j in range(pw):
            out[r1+1+i][c0+j] = mp2.get(pat_bl[i][j], 0)
    # regionBR
    seeds_br = [(i,j,grid[i][j]) for i in range(r1+1, r1+1+ph) for j in range(c1+1, c1+1+pw)
                if grid[i][j] not in (0,p0,p1)]
    if len(seeds_br) == 1:
        mp3 = {p0: 0, p1: seeds_br[0][2]}
    else:
        seedTR3 = nearest(seeds_br, r1+1, c1+pw)
        seedBL3 = nearest(seeds_br, r1+ph, c1+1)
        if len(seeds_br)>=2 and seeds_br[0][0] == seeds_br[1][0]:
            mp3 = {p0: seedTR3, p1: seedBL3}
        else:
            mp3 = {p0: seedBL3, p1: seedTR3}
    for i in range(ph):
        for j in range(pw):
            out[r1+1+i][c1+1+j] = mp3.get(pat_br[i][j], 0)
    return out