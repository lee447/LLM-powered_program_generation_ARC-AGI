def solve(grid):
    h = len(grid)
    w = len(grid[0])
    freq = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != 0:
                freq[v] = freq.get(v, 0) + 1
    if not freq:
        return grid
    target = max(freq, key=lambda k: freq[k])
    visited = [[False] * w for _ in range(h)]
    comps = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == target and not visited[i][j]:
                comps += 1
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == target:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
    min_r, max_r = h, -1
    min_c, max_c = w, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] == target:
                if i < min_r:
                    min_r = i
                if i > max_r:
                    max_r = i
                if j < min_c:
                    min_c = j
                if j > max_c:
                    max_c = j
    center_r = (min_r + max_r + 1) // 2
    center_c = (min_c + max_c + 1) // 2
    out = [row[:] for row in grid]
    if comps == 1:
        for j in range(w):
            out[center_r][j] = 3
    else:
        for i in range(h):
            out[i][center_c] = 3
    return out