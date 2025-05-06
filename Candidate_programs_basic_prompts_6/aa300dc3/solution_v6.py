def solve(grid):
    H=len(grid);W=len(grid[0])
    zeros={(r,c)for r in range(H)for c in range(W)if grid[r][c]==0}
    best_len=0;best_start=None;best_dir=(0,0)
    for dr,dc in((1,1),(1,-1)):
        for r,c in zeros:
            if (r-dr,c-dc)in zeros:continue
            length=0;rr,cc=r,c
            while (rr,cc)in zeros:
                length+=1;rr+=dr;cc+=dc
            if length>best_len:
                best_len=length;best_start=(r,c);best_dir=(dr,dc)
    out=[row[:]for row in grid]
    if best_start:
        r,c=best_start;dr,dc=best_dir
        for i in range(best_len):
            out[r+dr*i][c+dc*i]=8
    return out