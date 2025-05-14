def solve(grid):
    from collections import deque

    def bfs(start_i, start_j, target_color, new_color):
        queue = deque([(start_i, start_j)])
        visited = set()
        while queue:
            i, j = queue.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if grid[i][j] == target_color:
                grid[i][j] = new_color
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        queue.append((ni, nj))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 4:
                bfs(i, j, 0, 8)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 8:
                bfs(i, j, 0, 7)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 8:
                grid[i][j] = 0

    return grid