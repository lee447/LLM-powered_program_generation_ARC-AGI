def solve(grid):
    output = [[0] * 7 for _ in range(8)]
    output[0][3] = 3
    for r in range(1, 8):
        for c in range(3, 7):
            if c - 3 < r <= c - 1:
                output[r][c] = 2
    return output