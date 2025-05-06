from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n=len(grid); m=len(grid[0])
    out=[row[:] for row in grid]
    min_row=next(i for i,row in enumerate(grid) if any(c==0 for c in row))
    zeros_cols=[j for j,c in enumerate(grid[min_row]) if c==0]
    sr1,sc1=min_row,min(zeros_cols)
    sr2,sc2=min_row,max(zeros_cols)
    def count(sr,sc,dr,dc):
        r,c=sr,sc; cnt=0
        while 0<=r<n and 0<=c<m and grid[r][c]==0:
            cnt+=1; r+=dr; c+=dc
        return cnt
    c1=count(sr1,sc1,1,1)
    c2=count(sr2,sc2,1,-1)
    if c1>=c2:
        sr,sc,dr,dc,steps=sr1,sc1,1,1,c1
    else:
        sr,sc,dr,dc,steps=sr2,sc2,1,-1,c2
    for i in range(steps):
        r,c=sr+dr*i,sc+dc*i
        if out[r][c]==0: out[r][c]=8
    return out