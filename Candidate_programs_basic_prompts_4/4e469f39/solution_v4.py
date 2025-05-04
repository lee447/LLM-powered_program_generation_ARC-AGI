def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not seen[i][j]:
                # BFS to collect the component
                stack = [(i,j)]
                seen[i][j] = True
                comp = [(i,j)]
                for x,y in stack:
                    for dx,dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] == 5:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                            comp.append((nx,ny))
                # bounding box
                rs = [p[0] for p in comp]
                cs = [p[1] for p in comp]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                # fill all zeros in the box
                for r in range(r0, r1+1):
                    for c in range(c0, c1+1):
                        if out[r][c] == 0:
                            out[r][c] = 2
    return out