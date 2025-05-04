def solve(grid):
    H = len(grid)
    W = len(grid[0])
    sep = [i for i,row in enumerate(grid) if all(v==1 for v in row)]
    sep.sort()
    B = sep[1] - sep[0]
    exemplar = {}
    for offset in range(B):
        for i in range(offset, H, B):
            if all(v!=0 for v in grid[i]):
                exemplar[offset] = i
                break
    res = [row[:] for row in grid]
    for i in range(H):
        off = i % B
        exr = exemplar[off]
        for j in range(W):
            if grid[i][j] == 0:
                res[i][j] = grid[exr][j]
    return res