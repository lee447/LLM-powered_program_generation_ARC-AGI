from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    regs = sorted({c for row in grid for c in row if c != 0})
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[False]*w for _ in range(h)]
    out = [row[:] for row in grid]
    flips = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0 and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                comp = []
                is_border = False
                neighbor_colors = set()
                while q:
                    x, y = q.popleft()
                    comp.append((x, y))
                    if x in (0, h-1) or y in (0, w-1):
                        is_border = True
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w:
                            if grid[nx][ny] == 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                            elif grid[nx][ny] != 0:
                                neighbor_colors.add(grid[nx][ny])
                if is_border or len(neighbor_colors) != 1:
                    continue
                c = next(iter(neighbor_colors))
                other = regs[1] if regs[0] == c else regs[0]
                for x, y in comp:
                    out[x][y] = 8
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and out[nx][ny] == c:
                            flips.append((nx, ny, other))
    for x, y, oc in flips:
        out[x][y] = oc
    return out