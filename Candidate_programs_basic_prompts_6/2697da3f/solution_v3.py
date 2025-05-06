def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    if not pts:
        return grid
    minr = min(r for r, _ in pts)
    maxr = max(r for r, _ in pts)
    minc = min(c for _, c in pts)
    maxc = max(c for _, c in pts)
    Bh = maxr - minr + 1
    Bw = maxc - minc + 1
    B = [row[minc:maxc+1] for row in grid[minr:maxr+1]]
    if Bh == Bw:
        s = Bh + 2
        out_size = 2 * s + 1
    else:
        s = max(Bh, Bw) + 2
        out_size = 2 * s - 1
    pad_top = (s - Bh) // 2
    pad_left = (s - Bw) // 2
    C = [[0] * s for _ in range(s)]
    for r in range(Bh):
        for c in range(Bw):
            C[pad_top + r][pad_left + c] = B[r][c]
    def rot90(m):
        return [list(reversed(col)) for col in zip(*m)]
    def rot180(m):
        return [list(reversed(row)) for row in reversed(m)]
    def rot270(m):
        return [list(col) for col in reversed(list(zip(*m)))]
    Cs = [C, rot90(C), rot180(C), rot270(C)]
    out = [[0] * out_size for _ in range(out_size)]
    o = out_size
    a = (o - s) // 2
    pos = [
        (0, a),
        (a, o - s),
        (o - s, a),
        (a, 0)
    ]
    for (sr, sc), M in zip(pos, Cs):
        for i in range(s):
            for j in range(s):
                if M[i][j]:
                    out[sr + i][sc + j] = M[i][j]
    return out