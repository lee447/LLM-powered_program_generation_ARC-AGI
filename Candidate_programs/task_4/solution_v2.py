from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    bg = grid[0][0]
    visited = [[False]*C for _ in range(R)]
    shapes = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] != bg and not visited[i][j]:
                v = grid[i][j]
                stack = [(i, j)]
                visited[i][j] = True
                cells = []
                while stack:
                    x, y = stack.pop()
                    cells.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] == v:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                mr = min(x for x, _ in cells)
                shapes.append((mr, cells, v))
    shapes.sort(key=lambda x: x[0])
    out = [[bg]*C for _ in range(R)]
    for idx, (_, cells, v) in enumerate(shapes):
        shift = -1 if idx % 2 == 0 else 1
        for x, y in cells:
            out[x][y+shift] = v
    return out