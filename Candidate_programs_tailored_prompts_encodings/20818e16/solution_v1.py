def solve(grid):
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    seen = [[False]*w for _ in range(h)]
    rects = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c!=border and not seen[i][j]:
                stack=[(i,j)]
                seen[i][j]=True
                cells=[]
                while stack:
                    x,y=stack.pop()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==c:
                            seen[nx][ny]=True
                            stack.append((nx,ny))
                rs=[x for x,_ in cells]; cs=[y for _,y in cells]
                width = max(cs)-min(cs)+1
                rects.append((width,c))
    rects.sort(key=lambda x:x[0])
    ws=[r[0] for r in rects]
    cols = ws[-1]
    diffs = [ws[0], ws[1]-ws[0], ws[2]-ws[1]]
    colors = [r[1] for r in rects]
    bands = [ (colors[0], diffs[0]), (colors[1], diffs[1]), (colors[2], diffs[2]) ]
    height = sum(d for _,d in bands)
    out = [[0]*cols for _ in range(height)]
    row=0
    for colr, bh in bands:
        for _ in range(bh):
            pos=0
            for _,d in bands:
                run = d
                for k in range(run):
                    if pos<cols:
                        out[row][pos]=colr if d==bh and colr==colr else colr
                    pos+=1
            row+=1
    return out