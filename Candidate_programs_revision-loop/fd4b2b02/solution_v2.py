def solve(grid):
    R, C = len(grid), len(grid[0])
    pts = [(r, c) for r in range(R) for c in range(C) if grid[r][c] != 0]
    if not pts:
        return [[0] * C for _ in range(R)]
    color = grid[pts[0][0]][pts[0][1]]
    other = 6 if color == 3 else 3
    rs = [r for r, _ in pts]
    cs = [c for _, c in pts]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    h, w = r1 - r0 + 1, c1 - c0 + 1
    shape = [(r - r0, c - c0) for r, c in pts]
    rot = [(c - c0, r - r0) for r, c in pts]
    out = [[0] * C for _ in range(R)]
    rows = [0, r0, R - h]
    cols = [0, c0, C - w]
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                col = color; offs = shape; hh, ww = h, w
            elif i != 1 and j != 1:
                col = color; offs = shape; hh, ww = h, w
            else:
                col = other; offs = rot; hh, ww = w, h
            sr, sc = rows[i], cols[j]
            for dr, dc in offs:
                r, c = sr + dr, sc + dc
                if 0 <= r < R and 0 <= c < C:
                    out[r][c] = col
    return out