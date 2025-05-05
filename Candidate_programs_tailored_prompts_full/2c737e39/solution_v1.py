from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    greys = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5:
                greys.append((i, j))
    main = None
    anchor = None
    for i, j in greys:
        cnt = 0
        if i > 0 and grid[i-1][j] != 0: cnt += 1
        if i+1 < h and grid[i+1][j] != 0: cnt += 1
        if j > 0 and grid[i][j-1] != 0: cnt += 1
        if j+1 < w and grid[i][j+1] != 0: cnt += 1
        if cnt > 0:
            main = (i, j)
        else:
            anchor = (i, j)
    stack = [main]
    visited = set()
    cluster = []
    while stack:
        i, j = stack.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if grid[i][j] == 0:
            continue
        cluster.append((i, j, grid[i][j]))
        if i > 0 and (i-1, j) not in visited and grid[i-1][j] != 0:
            stack.append((i-1, j))
        if i+1 < h and (i+1, j) not in visited and grid[i+1][j] != 0:
            stack.append((i+1, j))
        if j > 0 and (i, j-1) not in visited and grid[i][j-1] != 0:
            stack.append((i, j-1))
        if j+1 < w and (i, j+1) not in visited and grid[i][j+1] != 0:
            stack.append((i, j+1))
    dr = anchor[0] - main[0]
    dc = anchor[1] - main[1]
    out = [row[:] for row in grid]
    out[anchor[0]][anchor[1]] = 0
    for i, j, val in cluster:
        if val == 5:
            continue
        ni = i + dr
        nj = j + dc
        if 0 <= ni < h and 0 <= nj < w:
            out[ni][nj] = val
    return out