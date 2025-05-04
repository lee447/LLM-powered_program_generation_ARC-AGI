def solve(grid):
    H, W = len(grid), len(grid[0])
    r0 = H; r1 = -1; c0 = W; c1 = -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0:
                r0 = min(r0, i); r1 = max(r1, i)
                c0 = min(c0, j); c1 = max(c1, j)
    h = r1 - r0 + 1; w = c1 - c0 + 1
    C0 = grid[r0][c0]
    C1 = 3 if C0 == 6 else 6
    pr = h + w; pc = h + w
    out = [[0]*W for _ in range(H)]
    for di in range(- (H//pr) - 2, (H//pr) + 3):
        for dj in range(- (W//pc) - 2, (W//pc) + 3):
            tr = r0 + di*pr
            tc = c0 + dj*pc
            if (di + dj) & 1 == 0:
                for dr in range(h):
                    for dc in range(w):
                        if grid[r0+dr][c0+dc] == C0:
                            rr, cc = tr+dr, tc+dc
                            if 0 <= rr < H and 0 <= cc < W:
                                out[rr][cc] = C0
            else:
                for dr in range(w):
                    for dc in range(h):
                        if grid[r0+dc][c0+dr] == C0:
                            rr, cc = tr+dr, tc+dc
                            if 0 <= rr < H and 0 <= cc < W:
                                out[rr][cc] = C1
    return out