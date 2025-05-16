def solve(grid):
    h,len_row = len(grid),len(grid[0])
    out = [row[:] for row in grid]
    regs = sorted({c for row in grid for c in row if c!=0})
    if len(regs)==2:
        c1,c2 = regs
        for r in range(h):
            for c in range(len_row):
                if grid[r][c]==0:
                    for C,other in ((c1,c2),(c2,c1)):
                        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                            rr,cc = r+dr,c+dc
                            if 0<=rr<h and 0<=cc<len_row and grid[rr][cc]==C:
                                out[r][c]=8
                                break
                        if out[r][c]==8:
                            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                                rr,cc = r+dr,c+dc
                                if 0<=rr<h and 0<=cc<len_row and grid[rr][cc]==C:
                                    out[rr][cc]=other
                            break
    return out