def solve(grid):
    H=len(grid); W=len(grid[0])
    blocks={}
    for r in range(H-1):
        for c in range(W-1):
            if grid[r][c]==8 and grid[r][c+1]==8 and grid[r+1][c]==8 and grid[r+1][c+1]==8:
                blocks.setdefault(r,[]).append(c)
    result=[]
    for r in sorted(blocks):
        cs=sorted(blocks[r])
        c0,c1=cs[0],cs[1]
        cols=list(range(c0+2,c1))
        for c in cs:
            re=r if c==c0 else r+1
            result.append([grid[re][x] for x in cols])
    return result