def solve(grid):
    H=len(grid); W=len(grid[0])
    spans=[]
    for r in range(H):
        c=0
        while c<=W-3:
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r][c+2]==2 and (c==0 or grid[r][c-1]!=2) and (c+3==W or grid[r][c+3]!=2):
                spans.append((r,c))
                c+=3
            else:
                c+=1
    if not spans:
        return grid
    best_score=-1; br=0; bc=spans[0][1]
    for sr,sc in spans:
        for r in range(H):
            score=0
            for dc in range(3):
                if grid[r][sc+dc]==0:
                    score+=1
            if score>best_score:
                best_score=score; br=r; bc=sc
    out=[row[:] for row in grid]
    for dc in range(3):
        out[br][bc+dc]=8
    return out