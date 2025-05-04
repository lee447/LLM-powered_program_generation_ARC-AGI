from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid); w=len(grid[0])
    pts=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==2:
                pts.append((i,j))
    (r1,c1),(r2,c2)=pts
    dx=0 if r2==r1 else (1 if r2>r1 else -1)
    dy=0 if c2==c1 else (1 if c2>c1 else -1)
    res=[row[:] for row in grid]
    r,c=r1,c1
    while True:
        if res[r][c]==0: res[r][c]=2
        elif res[r][c]==1: res[r][c]=3
        if r==r2 and c==c2: break
        r+=dx; c+=dy
    return res