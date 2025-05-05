def solve(grid):
    h, w = len(grid), len(grid[0])
    coords8 = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
    r1 = min(r for r, c in coords8)
    r2 = max(r for r, c in coords8)
    c1 = min(c for r, c in coords8)
    c2 = max(c for r, c in coords8)
    height = r2 - r1 + 1
    width = c2 - c1 + 1
    grey_row = 0
    for gr in range(r1 - 1, -1, -1):
        maxc = cur = 0
        for c in range(w):
            if grid[gr][c] == 5:
                cur += 1
                if cur > maxc: maxc = cur
            else:
                cur = 0
        if maxc >= width:
            grey_row = gr
            break
    left = 0
    for lc in range(c1 - 1, -1, -1):
        if grid[grey_row][lc] == 5:
            left = lc + 1
            break
    return [row[left:left + width] for row in grid[grey_row + 1:grey_row + 1 + height]]