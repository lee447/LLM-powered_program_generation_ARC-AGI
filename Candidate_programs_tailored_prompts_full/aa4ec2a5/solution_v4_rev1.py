def solve(grid):
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    ones = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 1]
    mapping = {1: 2, 2: 8, 3: 6}
    for d in (1, 2, 3):
        for r, c in ones:
            for dr in range(-d, d+1):
                for dc in range(-d, d+1):
                    if max(abs(dr), abs(dc)) != d:
                        continue
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < H and 0 <= cc < W and grid[rr][cc] != 1 and out[rr][cc] == grid[rr][cc]:
                        out[rr][cc] = mapping[d]
    return out