from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    sepR = [i for i in range(h) if all(c == 4 for c in grid[i])]
    sepC = [j for j in range(w) if all(grid[i][j] == 4 for i in range(h))]
    subRs = [(sepR[i]+1, sepR[i+1]-1) for i in range(len(sepR)-1) if sepR[i+1]-sepR[i]>1]
    subCs = [(sepC[j]+1, sepC[j+1]-1) for j in range(len(sepC)-1) if sepC[j+1]-sepC[j]>1]
    out = [row[:] for row in grid]
    for r0,r1 in subRs:
        for c0,c1 in subCs:
            cells = [(r,c) for r in range(r0,r1+1) for c in range(c0,c1+1)]
            vals = {grid[r][c] for r,c in cells if grid[r][c] not in (0,1,4)}
            if not vals: continue
            val = vals.pop()
            h0 = r1-r0+1; w0 = c1-c0+1
            midr = h0//2; midc = w0//2
            shape = [(r,c) for r,c in cells if grid[r][c]==val]
            minr = min(r-r0 for r,c in shape); minc = min(c-c0 for r,c in shape)
            top = minr < midr; left = minc < midc
            if top and left: dx,dy = 1,1
            elif top and not left: dx,dy = 1,-1
            elif not top and left: dx,dy = -1,1
            else: dx,dy = -1,-1
            cr,cc = r0+midr, c0+midc
            for dr,dc in ((dx,dy),(-dx,-dy)):
                rr,cc2 = cr+dr, cc+dc
                if 0<=rr<h and 0<=cc2<w and out[rr][cc2]==1:
                    out[rr][cc2] = val
    return out