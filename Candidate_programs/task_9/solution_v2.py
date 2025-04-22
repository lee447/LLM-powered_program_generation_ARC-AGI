def solve(grid):
    r = len(grid)
    c = len(grid[0])
    bs = r
    blocks = c // bs
    anti = {(i, bs - 1 - i) for i in range(bs)}
    colors = []
    for b in range(blocks):
        s = set()
        for i in range(bs):
            for j in range(bs):
                if grid[i][b * bs + j] == 5:
                    s.add((i, j))
        if s == anti:
            col = 9
        elif len(s) == 1:
            col = 4
        elif len(s) == bs and all(i == 0 for i, _ in s):
            col = 6
        elif len(s) == bs and all(i == bs - 1 for i, _ in s):
            col = 1
        elif len(s) == bs * bs - 1:
            col = 3
        else:
            col = 0
        colors.append(col)
    row = []
    for col in colors:
        row += [col] * bs
    return [row[:] for _ in range(bs)]