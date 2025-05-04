def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    stripe_cols = [j for j in range(cols) if all(grid[i][j] != 0 for i in range(rows))]
    stripe_colors = [grid[0][j] for j in stripe_cols]
    visited = [[False] * cols for _ in range(rows)]
    rects = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 8 and not visited[i][j]:
                w = 0
                while j + w < cols and grid[i][j + w] == 8 and not visited[i][j + w]:
                    w += 1
                h = 1
                while True:
                    if i + h >= rows:
                        break
                    ok = True
                    for c in range(j, j + w):
                        if grid[i + h][c] != 8 or visited[i + h][c]:
                            ok = False
                            break
                    if not ok:
                        break
                    h += 1
                cells = []
                for dr in range(h):
                    for dc in range(w):
                        visited[i + dr][j + dc] = True
                        cells.append((i + dr, j + dc))
                cx = sum(c for _, c in cells) / len(cells)
                rects.append((cx, cells))
    rects.sort(key=lambda x: x[0])
    out = [[0] * cols for _ in range(rows)]
    for color, (_, cells) in zip(stripe_colors, rects):
        for r, c in cells:
            out[r][c] = color
    return out