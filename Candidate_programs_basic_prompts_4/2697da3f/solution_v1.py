from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    pts=[(r,c) for r,row in enumerate(grid) for c,v in enumerate(row) if v!=0]
    rmin=min(r for r,c in pts); rmax=max(r for r,c in pts)
    cmin=min(c for r,c in pts); cmax=max(c for r,c in pts)
    ph=rmax-rmin+1; pw=cmax-cmin+1
    P0=[row[cmin:cmax+1] for row in grid[rmin:rmax+1]]
    def rot(M):
        a=len(M); b=len(M[0])
        return [[M[a-1-i][j] for i in range(a)] for j in range(b)]
    P90=rot(P0)
    P180=rot(P90)
    P270=rot(P180)
    H=pw+ph+pw; W=H
    out=[[0]*W for _ in range(H)]
    # place P0 at left-middle
    ro,co=pw,0
    for i in range(ph):
        for j in range(pw):
            out[ro+i][co+j]=P0[i][j]
    # place P90 at top-center
    ro,co=0,pw
    for i in range(len(P90)):
        for j in range(len(P90[0])):
            out[ro+i][co+j]=P90[i][j]
    # place P180 at right-middle
    ro,co=pw,pw+ph
    for i in range(len(P180)):
        for j in range(len(P180[0])):
            out[ro+i][co+j]=P180[i][j]
    # place P270 at bottom-center
    ro,co=pw+ph,pw
    for i in range(len(P270)):
        for j in range(len(P270[0])):
            out[ro+i][co+j]=P270[i][j]
    return out