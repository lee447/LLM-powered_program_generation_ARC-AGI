from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid);w=len(grid[0]);br=h//3;bc=w//3
    out=[[0]*w for _ in range(h)]
    for bi in range(br):
        for bj in range(bc):
            i0=bi*3;j0=bj*3
            c5=0
            for di in range(3):
                for dj in range(3):
                    if grid[i0+di][j0+dj]==5:
                        c5+=1
            if c5==8:
                c=3
            elif c5==1:
                c=4
            elif c5==3:
                if grid[i0+1][j0+1]==5:
                    c=9
                else:
                    top=True
                    for dj in range(3):
                        if grid[i0][j0+dj]!=5:
                            top=False
                    c=6 if top else 1
            else:
                c=0
            for di in range(3):
                for dj in range(3):
                    out[i0+di][j0+dj]=c
    return out