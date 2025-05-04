def solve(grid):
    h, w = len(grid), len(grid[0])
    pairs = []
    for r in range(h):
        c = 0
        while c < w - 1:
            if grid[r][c] == 2 and grid[r][c+1] == 2:
                pairs.append((r, c))
                c += 2
            else:
                c += 1
    out = [[0]*7 for _ in range(8)]
    out[0][3] = 3
    for i, (r0, c0) in enumerate(pairs):
        r1 = 1 + 2*i
        c1 = 3 + i
        for dr in (0, 1):
            if 0 <= r1+dr < 8:
                for dc in (0, 1):
                    if 0 <= c1+dc < 7:
                        out[r1+dr][c1+dc] = 2
    return out