def solve(grid):
    h, w = len(grid), len(grid[0])
    separators = [i for i in range(h) if all(grid[i][j] == 0 for j in range(w))]
    bands = []
    for i in range(len(separators) - 1):
        top, bottom = separators[i] + 1, separators[i+1]
        if top < bottom:
            bands.append((top, bottom))
    out = [row[:] for row in grid]
    for b, (top, bottom) in enumerate(bands):
        coords = [(r, c) for r in range(top, bottom) for c in range(w) if grid[r][c] == 2]
        if not coords:
            continue
        cols = sorted({c for _, c in coords})
        split_i = max(range(len(cols) - 1), key=lambda i: cols[i+1] - cols[i])
        left_max, right_min = cols[split_i], cols[split_i+1]
        left_set = {(r, c) for r, c in coords if c <= left_max}
        right_set = {(r, c) for r, c in coords if c >= right_min}
        target = right_set if b % 2 == 0 else left_set
        new_color = 8 if b < 2 else 3
        for r, c in target:
            if grid[r][c] == 2:
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    rr, cc = r+dr, c+dc
                    if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0:
                        out[r][c] = new_color
                        break
    return out