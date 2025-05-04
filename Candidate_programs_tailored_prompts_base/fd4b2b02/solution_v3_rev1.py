def solve(grid):
    H, W = len(grid), len(grid[0])
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] != 0]
    rs = [r for r, _ in pts]; cs = [c for _, c in pts]
    r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
    h, w = r1 - r0 + 1, c1 - c0 + 1
    c1col = grid[r0][c0]; c2col = 9 - c1col
    M = [[1 if grid[r0 + i][c0 + j] != 0 else 0 for j in range(w)] for i in range(h)]
    M2 = [[M[h - 1 - j][i] for j in range(h)] for i in range(w)]
    P = h + w
    out = [[0] * W for _ in range(H)]
    for a in range(-P, H + P, P):
        for b in range(-P, W + P, P):
            parity = ((a // P) + (b // P)) & 1
            if parity == 0:
                br, bc = r0 + a, c0 + b
                for i in range(h):
                    rr = br + i
                    if 0 <= rr < H:
                        for j in range(w):
                            cc = bc + j
                            if 0 <= cc < W and M[i][j]:
                                out[rr][cc] = c1col
            else:
                br, bc = r0 + a - (w - 1), c0 + b + (h - 1)
                for i in range(w):
                    rr = br + i
                    if 0 <= rr < H:
                        for j in range(h):
                            cc = bc + j
                            if 0 <= cc < W and M2[i][j]:
                                out[rr][cc] = c2col
    return out