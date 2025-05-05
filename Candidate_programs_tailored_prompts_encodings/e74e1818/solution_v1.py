def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    out = [row[:] for row in grid]
    i = 0
    while i < h:
        if any(cell != 0 for cell in grid[i]):
            start = i
            while i + 1 < h and any(cell != 0 for cell in grid[i + 1]):
                i += 1
            end = i
            height = end - start + 1
            if height > 1:
                sym = True
                for k in range(height):
                    if grid[start + k] != grid[end - k]:
                        sym = False
                        break
                if not sym:
                    for k in range(height):
                        out[start + k] = grid[end - k][:]
            i += 1
        else:
            i += 1
    return out