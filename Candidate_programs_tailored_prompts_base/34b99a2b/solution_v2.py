def solve(grid):
    rows, cols = len(grid), len(grid[0])
    stripe = next(j for j in range(cols) if all(grid[i][j] == 4 for i in range(rows)))
    others = [j for j in range(cols) if j != stripe]
    bw = len(others) // 4
    res = []
    for i in range(rows):
        row = []
        for b in range(4):
            seg = others[b*bw:(b+1)*bw]
            row.append(2 if any(grid[i][j] != 0 for j in seg) else 0)
        res.append(row)
    return res