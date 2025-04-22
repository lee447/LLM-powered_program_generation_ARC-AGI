def solve(grid):
    R, C = len(grid), len(grid[0])
    # find full-zero separator rows and cols
    sep_r = [r for r in range(R) if all(grid[r][c]==0 for c in range(C))]
    sep_c = [c for c in range(C) if all(grid[r][c]==0 for r in range(R))]
    # compute band height and block width
    bh = sep_r[1] - sep_r[0] - 1
    bw = sep_c[1] - sep_c[0] - 1
    # build motifs for interior size = bh-2
    m = bh-2
    motifs = []
    # full fill
    motifs.append([[True]*m for _ in range(m)])
    # diagonal
    motifs.append([[i==j for j in range(m)] for i in range(m)])
    # cross (plus)
    motifs.append([[i==m//2 or j==m//2 for j in range(m)] for i in range(m)])
    out = [row[:] for row in grid]
    # process each band
    for bi in range(len(sep_r)-1):
        r0 = sep_r[bi]+1
        # process each block in band
        for bj in range(len(sep_c)-1):
            c0 = sep_c[bj]+1
            # skip if no border
            color = None
            for c in range(c0, c0+bw):
                if grid[r0][c]!=0:
                    color = grid[r0][c]
                    break
            if not color: continue
            motif = motifs[bj]
            for i in range(m):
                for j in range(m):
                    if motif[i][j]:
                        out[r0+1+i][c0+1+j] = color
    return out