import numpy as np
def solve(grid):
    row=grid[0]
    n=len(row)
    mid=row.index(2)
    out=[[0]*n for _ in range(n)]
    for r in range(mid+1):
        out[r][mid-r]=2
        out[r][mid+r]=2
    for r in range(3,n):
        left=mid-r; right=mid+r
        for c in range(n):
            if out[r][c]==0 and (r-c+mid)%4==0 and (r>mid or left<c<right):
                out[r][c]=1
    return out