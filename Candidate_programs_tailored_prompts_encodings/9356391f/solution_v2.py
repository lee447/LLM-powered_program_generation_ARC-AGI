def solve(grid):
    h, w = len(grid), len(grid[0])
    palette = [grid[0][c] for c in range(w) if grid[0][c] != 0]
    anchor = None
    for y in range(h // 2, h):
        for x in range(w):
            if grid[y][x] != 0:
                anchor = (y, x)
                break
        if anchor:
            break
    ay, ax = anchor
    for idx in range(len(palette) - 1, -1, -1):
        r = idx
        c = palette[idx]
        for dy in range(-r, r + 1):
            y = ay + dy
            if y <= 1 or y < 0 or y >= h:
                continue
            for dx in range(-r, r + 1):
                x = ax + dx
                if x < 0 or x >= w:
                    continue
                grid[y][x] = c
    return grid