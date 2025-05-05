def solve(grid):
    h=len(grid); w=len(grid[0])
    greys=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==5]
    by_row={}
    by_col={}
    for r,c in greys:
        by_row.setdefault(r,[]).append(c)
        by_col.setdefault(c,[]).append(r)
    for r,cols in by_row.items():
        if len(cols)>1 and r+1<h:
            min_c,mincc=min(cols),max(cols)
            sc=[c for c in range(min_c,mincc+1) if 0<=r+1<h and grid[r+1][c]!=0 and grid[r+1][c]!=5]
            if sc:
                sc0=sc[0]
                sr=[]
                rr=r+1
                while rr<h and grid[rr][sc0]!=0 and grid[rr][sc0]!=5:
                    sr.append(rr); rr+=1
                vals=[grid[x][sc0] for x in sr]
                for i,rr in enumerate(sr):
                    v=vals[i]
                    for c in range(min_c,mincc+1):
                        grid[rr][c]=v
    for c,rows in by_col.items():
        if len(rows)>1 and c+1<w:
            min_r,maxr=min(rows),max(rows)
            sr=[r for r in range(min_r,maxr+1) if 0<=c+1<w and grid[r][c+1]!=0 and grid[r][c+1]!=5]
            if sr:
                fr=sr[0]
                width=0; cc=c+1
                while cc<w and grid[fr][cc]!=0 and grid[fr][cc]!=5:
                    width+=1; cc+=1
                block=[ [grid[r][c+1+i] for i in range(width)] for r in sr ]
                bar=sorted(rows)
                m=len(block)
                for i,r in enumerate(bar):
                    rowvals=block[i%m]
                    for j,v in enumerate(rowvals):
                        grid[r][c+1+j]=v
    return grid