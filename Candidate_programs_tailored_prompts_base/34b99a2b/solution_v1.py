def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    stripe = next(j for j in range(cols) if any(grid[i][j] == 4 for i in range(rows)))
    left = stripe
    right = cols - stripe - 1
    lb = left // 2
    rb = right // 2
    bands = [(0, lb), (lb, stripe), (stripe+1, stripe+1+rb), (stripe+1+rb, cols)]
    out = []
    for i in range(rows):
        row = []
        for a, b in bands:
            v = 0
            for j in range(a, b):
                if grid[i][j] != 0:
                    v = 2
                    break
            row.append(v)
        out.append(row)
    return out