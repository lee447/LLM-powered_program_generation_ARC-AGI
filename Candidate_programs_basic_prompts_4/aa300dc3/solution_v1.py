from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R=len(grid); C=len(grid[0])
    best_len=0; best=None
    for r in range(R):
        for c in range(C):
            if grid[r][c]!=0: continue
            for dr,dc in ((1,1),(1,-1)):
                pr,pc=r-dr,c-dc
                if 0<=pr<R and 0<=pc<C and grid[pr][pc]==0: continue
                k=0
                while True:
                    nr,nc=r+dr*k,c+dc*k
                    if 0<=nr<R and 0<=nc<C and grid[nr][nc]==0:
                        k+=1
                    else:
                        break
                if k>best_len:
                    best_len=k; best=(r,c,dr,dc)
    out=[row[:] for row in grid]
    if best:
        r0,c0,dr,dc=best
        for k in range(best_len):
            out[r0+dr*k][c0+dc*k]=8
    return out