def solve(grid):
    h, w = len(grid), len(grid[0])
    border_color = next(c for c in grid[-1] if c != 0)
    anchor_row = h - 2
    anchors = [i for i, c in enumerate(grid[anchor_row]) if c == border_color]
    anchor_set = set(anchors)
    visited = [[False] * w for _ in range(h)]
    clusters = []
    for r in range(anchor_row):
        for c in range(w):
            if grid[r][c] != 0 and not visited[r][c]:
                color = grid[r][c]
                stack = [(r, c)]
                pts = []
                visited[r][c] = True
                while stack:
                    y, x = stack.pop()
                    pts.append((y, x))
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < anchor_row and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == color:
                            visited[ny][nx] = True
                            stack.append((ny, nx))
                clusters.append((len(pts), min(x for y, x in pts), color))
    clusters.sort(key=lambda x: (x[0], x[1]))
    newg = [[0] * w for _ in range(h)]
    for x in range(w):
        newg[-1][x] = border_color
    for a in anchors:
        newg[anchor_row][a] = border_color
    used = set()
    occupied = set()
    for size, _, color in clusters:
        width = size // 2
        for a in anchors:
            if a in used: continue
            base = a + 1
            if base + width <= w:
                cols = set(range(base, base + width))
                if cols & anchor_set: continue
                if cols & occupied: continue
                anchor = a
                break
        used.add(anchor)
        cols = range(anchor + 1, anchor + 1 + width)
        for c in cols:
            newg[anchor_row][c] = color
            newg[anchor_row - 1][c] = color
        occupied |= set(cols)
    return newg