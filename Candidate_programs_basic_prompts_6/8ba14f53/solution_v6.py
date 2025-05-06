def solve(grid):
    h, w = len(grid), len(grid[0])
    bw = w // 3
    out = [[0]*3 for _ in range(3)]
    for b in range(3):
        block = [row[b*bw:(b+1)*bw] for row in grid[:3]]
        cols = list(zip(*block))
        for i in range(3):
            col = cols[i]
            nz = [c for c in col if c!=0]
            out[i][b] = nz[0] if len(nz)==1 else (max(set(nz), key=nz.count) if nz else 0)
    return out