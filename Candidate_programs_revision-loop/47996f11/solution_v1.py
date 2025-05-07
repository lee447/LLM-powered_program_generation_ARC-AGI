def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,-1),(1,1),(-1,-1),(-1,1)]
    g = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==6 and not vis[i][j]:
                comp = [(i,j)]
                vis[i][j] = True
                stack = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==6:
                            vis[nx][ny]=True
                            stack.append((nx,ny))
                            comp.append((nx,ny))
                best = None
                for d in dirs:
                    seen, fail = {}, 0
                    for x,y in comp:
                        dx,dy = d
                        k = 1
                        val = None
                        while True:
                            nx,ny = x+dx*k, y+dy*k
                            if not (0<=nx<h and 0<=ny<w): 
                                fail += 1
                                break
                            if grid[nx][ny]!=6:
                                val = grid[nx][ny]
                                seen[val] = seen.get(val,0)+1
                                break
                            k += 1
                    if best is None or (fail, len(seen)) < best[0]:
                        best = ((fail, len(seen)), d, seen)
                _, (dr,dc), seen = best
                # choose the most frequent neighbor value
                mode = max(seen.items(), key=lambda x:x[1])[0]
                for x,y in comp:
                    k = 1
                    while True:
                        nx,ny = x+dr*k, y+dc*k
                        if not (0<=nx<h and 0<=ny<w) or grid[nx][ny]!=6:
                            if 0<=nx<h and 0<=ny<w and grid[nx][ny]!=6:
                                g[x][y] = grid[nx][ny]
                            else:
                                g[x][y] = mode
                            break
                        k += 1
    return g