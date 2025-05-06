from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    orig = grid
    res = [row[:] for row in grid]
    outside_zero = [[False]*w for _ in range(h)]
    dq = deque()
    for i in range(h):
        for j in (0, w-1):
            if orig[i][j] == 0 and not outside_zero[i][j]:
                outside_zero[i][j] = True
                dq.append((i, j))
    for j in range(w):
        for i in (0, h-1):
            if orig[i][j] == 0 and not outside_zero[i][j]:
                outside_zero[i][j] = True
                dq.append((i, j))
    while dq:
        x, y = dq.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w and orig[nx][ny] == 0 and not outside_zero[nx][ny]:
                outside_zero[nx][ny] = True
                dq.append((nx, ny))
    barrier1 = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if orig[i][j] == 1:
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < h and 0 <= nj < w and outside_zero[ni][nj]:
                        barrier1[i][j] = True
                        break
    allowed1 = [[orig[i][j] == 1 and not barrier1[i][j] for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            c = orig[i][j]
            if c > 1:
                dq = deque([(i, j)])
                while dq:
                    x, y = dq.popleft()
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and allowed1[nx][ny] and res[nx][ny] == 1:
                            res[nx][ny] = c
                            dq.append((nx, ny))
    return res