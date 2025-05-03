def solve(grid):
    R=len(grid)
    C=len(grid[0])
    seed=[grid[R-1-i][::-1] for i in range(R)]
    seedH=[row[::-1] for row in seed]
    seedV=seed[::-1]
    seedHV=[row[::-1] for row in seedV]
    out=[]
    for i in range(R):
        out.append(seed[i]+seedH[i])
    for i in range(R):
        out.append(seedV[i]+seedHV[i])
    return out