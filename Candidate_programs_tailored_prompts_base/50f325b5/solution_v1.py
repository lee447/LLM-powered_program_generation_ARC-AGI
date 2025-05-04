def solve(grid):
    h, w = len(grid), len(grid[0])
    # find the horizontal 8‐bar template
    template = None
    for r in range(h):
        c = 0
        while c < w:
            if grid[r][c] == 8:
                start = c
                while c < w and grid[r][c] == 8:
                    c += 1
                length = c - start
                if template is None or length > len(template):
                    template = [8] * length
            else:
                c += 1
    if not template:
        return grid
    L = len(template)
    # stamp template onto every horizontal run of L greens
    for r in range(h):
        for c in range(w - L + 1):
            if all(grid[r][c + k] == 3 for k in range(L)):
                for k in range(L):
                    grid[r][c + k] = template[k]
    return grid