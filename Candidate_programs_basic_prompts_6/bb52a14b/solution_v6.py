def solve(grid):
    H=len(grid);W=len(grid[0])
    out=[row[:] for row in grid]
    blocks={}
    for r in range(H-2):
        for c in range(W-2):
            b=tuple(tuple(grid[r+dr][c+dc] for dc in range(3)) for dr in range(3))
            vals={v for row in b for v in row}
            if vals<={1,4,8} and vals&{1,4,8} and b not in blocks:
                blocks[b]=(r,c)
    for b,(r,c) in blocks.items():
        c1=W-(c+3)
        if 0<=c1<=W-3 and all(grid[r+dr][c1+dc]==0 for dr in range(3) for dc in range(3)):
            for dr in range(3):
                for dc in range(3):
                    out[r+dr][c1+dc]=b[dr][dc]
        r2=c-(3-1);c2=W-(r+3)
        if 0<=r2<=H-3 and 0<=c2<=W-3 and all(grid[r2+dr][c2+dc]==0 for dr in range(3) for dc in range(3)):
            for dr in range(3):
                for dc in range(3):
                    out[r2+dr][c2+dc]=b[dr][dc]
    return out