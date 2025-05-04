import collections
def solve(grid):
    h,len_row = len(grid), len(grid[0])
    w = len_row
    seen = [[False]*w for _ in range(h)]
    rects = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==3 and not seen[i][j]:
                stack=[(i,j)]
                seen[i][j]=True
                cells=[]
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]==3 and not seen[nr][nc]:
                            seen[nr][nc]=True
                            stack.append((nr,nc))
                rs=[r for r,c in cells]
                cs=[c for r,c in cells]
                rects.append((min(rs),max(rs),min(cs),max(cs)))
    out = [row[:] for row in grid]
    by_row = collections.defaultdict(list)
    by_col = collections.defaultdict(list)
    for r0,r1,c0,c1 in rects:
        by_row[(r0,r1)].append((r0,r1,c0,c1))
        by_col[(c0,c1)].append((r0,r1,c0,c1))
    for (r0,r1),sh in by_row.items():
        sh.sort(key=lambda x:x[2])
        y1,y2 = r0+1, r1-1
        for a,b,c0,c1 in zip(sh, sh[1:], [0]*len(sh), [0]*len(sh)):
            left=a; right=b
            x0,x1 = left[3], right[2]
            for x in range(x0, x1+1):
                out[y1][x]=3; out[y2][x]=3
    for (c0,c1),sh in by_col.items():
        sh.sort(key=lambda x:x[0])
        x1,x2 = c0+1, c1-1
        for a,b in zip(sh, sh[1:]):
            up,down = a,b
            y0,y1 = up[1], down[0]
            for y in range(y0, y1+1):
                out[y][x1]=3; out[y][x2]=3
    return out