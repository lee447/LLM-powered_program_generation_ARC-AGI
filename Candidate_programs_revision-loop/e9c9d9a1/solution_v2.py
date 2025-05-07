from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R=len(grid); C=len(grid[0])
    row_seps=[i for i in range(R) if all(grid[i][j]==3 for j in range(C))]
    col_seps=[j for j in range(C) if all(grid[i][j]==3 for i in range(R))]
    def intervals(seps, N):
        res=[]; prev=-1
        for s in seps:
            if s-prev>1:
                res.append((prev+1, s-1))
            prev=s
        if N-1-prev>0:
            res.append((prev+1, N-1))
        return res
    row_int=intervals(row_seps, R)
    col_int=intervals(col_seps, C)
    BR=len(row_int); BC=len(col_int)
    out=[row[:] for row in grid]
    for br,(rs,re) in enumerate(row_int):
        for bc,(cs,ce) in enumerate(col_int):
            color=None
            if br==0 and bc==0: color=2
            elif br==0 and bc==BC-1: color=4
            elif br==BR-1 and bc==0: color=1
            elif br==BR-1 and bc==BC-1: color=8
            elif 0<br<BR-1 and 0<bc<BC-1: color=7
            if color is not None:
                for i in range(rs,re+1):
                    for j in range(cs,ce+1):
                        if out[i][j]==0:
                            out[i][j]=color
    return out