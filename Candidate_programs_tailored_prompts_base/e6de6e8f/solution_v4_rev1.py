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
    for i, _ in enumerate(pairs):
        r1 = 1 + 2*i
        if grid[0][0] == 2:
            c1 = 3
        else:
            c1 = 2
        if i % 2 == 0:
            for dr in (0, 1):
                for dc in (0, 1):
                    rr, cc = r1 + dr, c1 + i + dc
                    if 0 <= rr < 8 and 0 <= cc < 7:
                        out[rr][cc] = 2
        else:
            for dr in (0, 1):
                rr, cc = r1 + dr, c1 + i
                if 0 <= rr < 8 and 0 <= cc < 7:
                    out[rr][cc] = 2
    return out