def solve(grid):
    h = len(grid)
    bh = h // 3
    output = []
    for b in range(3):
        cells = []
        for i in range(b * bh, (b + 1) * bh):
            for j, v in enumerate(grid[i]):
                if v != 0:
                    cells.append((j, v))
        cells.sort(key=lambda x: x[0])
        output.append([v for _, v in cells])
    return output