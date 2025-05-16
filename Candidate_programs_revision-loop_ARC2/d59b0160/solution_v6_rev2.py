from collections import deque
def solve(grid):
    n, m = len(grid), len(grid[0])
    bg = max(range(10), key=lambda c: sum(row.count(c) for row in grid))
    seen = [[False]*m for _ in range(n)]
    best_comp = []
    best_size = 0
    for i in range(n):
        for j in range(m):
            if not seen[i][j] and grid[i][j] != bg and grid[i][j] != 3:
                comp = []
                zeros = 0
                dq = deque([(i, j)])
                seen[i][j] = True
                while dq:
                    x, y = dq.popleft()
                    comp.append((x, y))
                    if grid[x][y] == 0:
                        zeros += 1
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m and not seen[nx][ny]:
                            if grid[nx][ny] != bg and grid[nx][ny] != 3:
                                seen[nx][ny] = True
                                dq.append((nx, ny))
                size = len(comp)
                if zeros*2 > size and size > best_size:
                    best_comp = comp
                    best_size = size
    out = [row[:] for row in grid]
    for x, y in best_comp:
        out[x][y] = bg
    return out