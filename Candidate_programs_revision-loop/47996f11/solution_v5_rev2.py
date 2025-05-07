def solve(grid):
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    dirs = [(-1,-1),(-1,1),(1,-1),(1,1),(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 6 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                region = []
                while stack:
                    x,y = stack.pop()
                    region.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 6:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                best_fail = float('inf')
                best_seen = set()
                best_dir = None
                for dr,dc in dirs:
                    fail = 0
                    seen = set()
                    for x,y in region:
                        k = 1
                        while True:
                            nx,ny = x+dr*k, y+dc*k
                            if not (0 <= nx < h and 0 <= ny < w):
                                fail += 1
                                break
                            v = grid[nx][ny]
                            if v != 6:
                                seen.add(v)
                                break
                            k += 1
                    if fail < best_fail or (fail == best_fail and len(seen) > len(best_seen)):
                        best_fail, best_seen, best_dir = fail, seen, (dr,dc)
                dr,dc = best_dir
                if best_fail < len(region):
                    for x,y in region:
                        k = 1
                        while True:
                            nx,ny = x+dr*k, y+dc*k
                            if not (0 <= nx < h and 0 <= ny < w):
                                break
                            v = grid[nx][ny]
                            if v != 6:
                                g[x][y] = v
                                break
                            k += 1
    return g