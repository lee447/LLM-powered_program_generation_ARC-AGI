from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                q = deque([(i, j)])
                visited[i][j] = True
                comp = []
                min_r = i; max_r = i; min_c = j; max_c = j
                while q:
                    x, y = q.popleft()
                    comp.append((x, y))
                    if x < min_r: min_r = x
                    if x > max_r: max_r = x
                    if y < min_c: min_c = y
                    if y > max_c: max_c = y
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == col:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                clusters.append((min_r, min_c, max_r, max_c, comp))
    clusters.sort(key=lambda x: (-x[0], x[1]))
    min_r, min_c, max_r, max_c, comp = clusters[0]
    H = max_r - min_r + 1
    W = max_c - min_c + 1
    out = [[0]*W for _ in range(H)]
    for r, c in comp:
        out[r-min_r][c-min_c] = grid[r][c]
    return out