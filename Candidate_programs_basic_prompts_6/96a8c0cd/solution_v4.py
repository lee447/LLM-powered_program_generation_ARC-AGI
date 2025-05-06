from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    centers: List[Tuple[int,int]] = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                cells = [(i,j)]
                while stack:
                    y,x = stack.pop()
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==col:
                            visited[ny][nx] = True
                            stack.append((ny,nx))
                            cells.append((ny,nx))
                ys = [y for y,x in cells]
                xs = [x for y,x in cells]
                cy = (min(ys)+max(ys))//2
                cx = (min(xs)+max(xs))//2
                centers.append((cy,cx))
    def draw(y0,x0,y1,x1):
        y,x = y0,x0
        dy = 1 if y1>y0 else -1
        while y!=y1:
            if grid[y][x]==0: grid[y][x]=2
            y += dy
        dx = 1 if x1>x0 else -1
        while x!=x1:
            if grid[y][x]==0: grid[y][x]=2
            x += dx
        if grid[y][x]==0: grid[y][x]=2
    by_x = sorted(centers, key=lambda p: p[1])
    for a,b in zip(by_x, by_x[1:]):
        draw(a[0],a[1],b[0],b[1])
    by_y = sorted(centers, key=lambda p: p[0])
    for a,b in zip(by_y, by_y[1:]):
        draw(a[0],a[1],b[0],b[1])
    return grid