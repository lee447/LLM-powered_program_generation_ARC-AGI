def solve(grid):
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    visited = [[False]*w for _ in range(h)]
    regions = []
    for y in range(h):
        for x in range(w):
            if not visited[y][x] and grid[y][x] != border:
                color = grid[y][x]
                stack = [(y, x)]
                visited[y][x] = True
                cells = []
                top = y
                while stack:
                    cy, cx = stack.pop()
                    cells.append((cy, cx))
                    if cy < top: top = cy
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == color:
                            visited[ny][nx] = True
                            stack.append((ny, nx))
                regions.append((top, color, cells))
    regions.sort(key=lambda r: r[0])
    new = [[border]*w for _ in range(h)]
    for i, (_, color, cells) in enumerate(regions):
        shift = -1 if i%2==0 else 1
        for y, x in cells:
            new[y][x+shift] = color
    return new