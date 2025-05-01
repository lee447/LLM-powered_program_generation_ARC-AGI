from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid);w=len(grid[0])
    minr=next((i for i in range(h) if any(grid[i][j]!=0 for j in range(w))),h)
    shifts=[0,-1,0,1]
    out=[[0]*w for _ in range(h)]
    for i in range(h):
        off=shifts[(i-minr)%4] if i>=minr else 0
        for j,v in enumerate(grid[i]):
            if v!=0:
                nj=j+off
                if 0<=nj<w:
                    out[i][nj]=v
    return out