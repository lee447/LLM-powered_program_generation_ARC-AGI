def solve(grid):
    H, W = len(grid), len(grid[0])
    squares = []
    for i in range(H - 3):
        for j in range(W - 3):
            c = grid[i][j]
            if c != 0 and all(grid[i][j + k] == c for k in range(4)) and all(grid[i + 3][j + k] == c for k in range(4)) and all(grid[i + k][j] == c for k in range(4)) and all(grid[i + k][j + 3] == c for k in range(4)) and all(grid[i + r][j + c_] == 0 for r in (1, 2) for c_ in (1, 2)):
                squares.append((i, j, c))
    squares.sort(key=lambda x: x[0] + x[1])
    n = len(squares) // 2
    sel = squares[:n]
    ys = [i for i, j, c in sel]
    xs = [j for i, j, c in sel]
    horiz = max(ys) - min(ys) < max(xs) - min(xs)
    out = []
    if horiz:
        for di in range(4):
            row = []
            for i, j, c in sel:
                row += [c if (di in (0, 3) and 0 <= dc < 4) or (dc in (0, 3) and 0 <= di < 4) else 0 for dc in range(4)]
            out.append(row)
    else:
        for i, j, c in sel:
            for di in range(4):
                out.append([c if (di in (0, 3) and 0 <= dc < 4) or (dc in (0, 3) and 0 <= di < 4) else 0 for dc in range(4)])
    return out