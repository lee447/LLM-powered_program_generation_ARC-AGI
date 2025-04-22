from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    sepr, sepc = [i for i in range(h) if all(grid[i][j]==0 for j in range(w))], [j for j in range(w) if all(grid[i][j]==0 for i in range(h))]
    out = [row[:] for row in grid]
    for bi in range(len(sepr)-1):
        for bj in range(len(sepc)-1):
            r0, r1 = sepr[bi]+1, sepr[bi+1]
            c0, c1 = sepc[bj]+1, sepc[bj+1]
            block_dim = r1-r0
            colors = {grid[r][c] for r in range(r0,r1) for c in range(c0,c1) if grid[r][c]!=0}
            if len(colors)!=2: continue
            a,b = sorted(colors)
            corners = [grid[r0][c0], grid[r0][c1-1], grid[r1-1][c0], grid[r1-1][c1-1]]
            cur = corners[0] if all(x==corners[0] for x in corners) else (a if corners.count(a)>0 else b)
            other = (a+b)-cur
            if (bi+bj)&1==0:
                shape_col, fill_col = other, cur
            else:
                shape_col, fill_col = cur, other
            s = block_dim//2
            shapepos = set()
            for i in range(s):
                shapepos |= {(0,i),(i,0),(0,block_dim-1-i),(i,block_dim-1),(block_dim-1,i),(block_dim-1-i,0),(block_dim-1,block_dim-1-i),(block_dim-1-i,block_dim-1)}
            for r in range(r0,r1):
                for c in range(c0,c1):
                    dr,dc = r-r0, c-c0
                    if (dr,dc) in shapepos:
                        out[r][c] = shape_col
                    else:
                        out[r][c] = fill_col
    return out