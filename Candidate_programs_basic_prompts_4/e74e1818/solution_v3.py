def solve(grid):
    h=len(grid); w=len(grid[0])
    out=[[0]*w for _ in range(h)]
    visited=[[False]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if grid[y][x]!=0 and not visited[y][x]:
                col=grid[y][x]
                stack=[(y,x)]; comp=[]
                visited[y][x]=True
                while stack:
                    cy,cx=stack.pop()
                    comp.append((cy,cx))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy+dy, cx+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==col:
                            visited[ny][nx]=True
                            stack.append((ny,nx))
                ys=[p[0] for p in comp]; xs=[p[1] for p in comp]
                miny, maxy = min(ys), max(ys)
                for cy,cx in comp:
                    ny = miny+maxy-cy
                    out[ny][cx] = col
    return out