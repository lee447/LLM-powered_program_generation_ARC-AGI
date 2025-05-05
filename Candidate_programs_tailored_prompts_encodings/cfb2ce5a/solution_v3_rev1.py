from typing import List
import math

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    nz = [(r, c) for r in range(H) for c in range(W) if grid[r][c] != 0]
    nz.sort()
    r0, c0 = nz[0]
    w = 0
    while c0 + w < W and grid[r0][c0 + w] != 0:
        w += 1
    h = 0
    while r0 + h < H and grid[r0 + h][c0] != 0:
        h += 1
    N = min(w, h)
    block = [row[c0:c0+N] for row in grid[r0:r0+N]]
    a, b = sorted({v for row in block for v in row})
    def pick_coords(rs, re, cs, ce, k=None):
        pts = []
        for i in range(rs, re):
            for j in range(cs, ce):
                v = grid[i][j]
                if v != 0:
                    pts.append((i, j, v))
                    if k and len(pts) >= k:
                        return pts
        return pts
    out = [[0]*W for _ in range(H)]
    for i in range(N):
        for j in range(N):
            out[r0+i][c0+j] = block[i][j]
    # TR
    blockCW = [[block[N-1-j][i] for j in range(N)] for i in range(N)]
    seedsTR = pick_coords(r0, r0+N, c0+N, c0+2*N, 2)
    mapTR = {}
    for r, c, v in seedsTR:
        i, j = r - r0, c - (c0 + N)
        col = blockCW[i][j]
        mapTR[col] = v
    for i in range(N):
        for j in range(N):
            out[r0+i][c0+N+j] = mapTR[blockCW[i][j]]
    # BL
    blockCCW = [[block[j][N-1-i] for j in range(N)] for i in range(N)]
    seedsBL = pick_coords(r0+N, r0+2*N, c0, c0+N, 2)
    mapBL = {}
    for r, c, v in seedsBL:
        i, j = r - (r0 + N), c - c0
        col = blockCCW[i][j]
        mapBL[col] = v
    for i in range(N):
        for j in range(N):
            out[r0+N+i][c0+j] = mapBL[blockCCW[i][j]]
    # BR
    seedsBR = pick_coords(r0+N, r0+2*N, c0+N, c0+2*N)
    pts = [(r-(r0+N), c-(c0+N), v) for r,c,v in seedsBR]
    if pts:
        drs = [d for d,_,_ in pts]
        dcs = [c for _,c,_ in pts]
        tile_h = max(drs) - min(drs) + 1
        tile_w = max(dcs) - min(dcs) + 1
        reps_i = math.ceil(N / tile_h)
        reps_j = math.ceil(N / tile_w)
        for dr, dc, v in pts:
            for ti in range(reps_i):
                for tj in range(reps_j):
                    i = r0 + N + dr + ti*tile_h
                    j = c0 + N + dc + tj*tile_w
                    if r0+N <= i < r0+2*N and c0+N <= j < c0+2*N:
                        out[i][j] = v
    return out