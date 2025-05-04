def solve(grid):
    h = len(grid)
    w = len(grid[0])
    base = grid[h-1][0]
    mask = grid[h-2]
    drops = [i for i,x in enumerate(mask) if x==0]
    segs = []
    for x in drops:
        if not segs or x!=segs[-1][-1]+1:
            segs.append([x])
        else:
            segs[-1].append(x)
    visited = [[False]*w for _ in range(h)]
    shapes = []
    for r in range(h-2):
        for c in range(w):
            if grid[r][c]!=0 and not visited[r][c]:
                col = grid[r][c]
                stack = [(r,c)]
                visited[r][c] = True
                cells = []
                while stack:
                    y,x = stack.pop()
                    cells.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0<=ny<h-2 and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==col:
                            visited[ny][nx] = True
                            stack.append((ny,nx))
                minc = min(x for y,x in cells)
                minr = min(y for y,x in cells)
                shapes.append((minc,minr,col,len(cells)))
    shapes.sort(key=lambda x:(x[0],x[1]))
    out = [[0]*w for _ in range(h)]
    out[h-1] = [base]*w
    for (minc,minr,col,cnt), seg in zip(shapes, segs):
        L = len(seg)
        H = cnt//L
        for dy in range(H):
            for dx in range(L):
                out[h-2-dy][seg[dx]] = col
    return out