def solve(grid):
    h, w = len(grid), len(grid[0])
    half = w // 2
    left = [row[:half] for row in grid]
    right = [row[half:] for row in grid]
    vis = [[False]*half + [False]*half for _ in range(h)]
    shapes = []
    for r in range(h):
        for c in range(half, w):
            if grid[r][c] != 0 and not vis[r][c]:
                col = grid[r][c]
                stack = [(r,c)]
                comp = []
                vis[r][c] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and half <= ny < w and not vis[nx][ny] and grid[nx][ny]==col:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                rs = [p[0] for p in comp]
                shapes.append((min(rs), max(rs), col))
    shapes.sort(key=lambda x: x[0])
    base = next(v for row in left for v in row if v!=0)
    cols = [c for _,_,c in shapes]
    if base < min(cols):
        region_cols = cols[1:]+cols[:1]
    else:
        region_cols = cols[::-1]
    res = [row[:] for row in left]
    for (r0,r1,_), col in zip(shapes, region_cols):
        for r in range(r0, r1+1):
            for c in range(half):
                if left[r][c]==0:
                    res[r][c] = col
    return res