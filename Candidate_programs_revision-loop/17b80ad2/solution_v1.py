from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid); w=len(grid[0])
    out=[row.copy() for row in grid]
    stripe_row=0
    for i in range(h-1,-1,-1):
        if any(grid[i][j]!=0 for j in range(w)):
            stripe_row=i
            break
    stripe_cols=[j for j in range(w) if grid[stripe_row][j]==5]
    for col in stripe_cols:
        anchors=[(r,grid[r][col]) for r in range(h) if grid[r][col]!=0]
        if not anchors: continue
        anchors.sort()
        r0,v0=anchors[0]
        for r in range(0,r0):
            out[r][col]=v0
        for (r_prev,v_prev),(r_curr,v_curr) in zip(anchors,anchors[1:]):
            for r in range(r_prev+1,r_curr):
                out[r][col]=v_curr
    return out