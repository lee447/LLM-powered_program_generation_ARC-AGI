def solve(grid):
    h, w = len(grid), len(grid[0])
    coords_by_color = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            coords_by_color.setdefault(v, []).append((i, j))
    def is_frame(c):
        pts = coords_by_color.get(c, [])
        if not pts:
            return False
        rs = [p[0] for p in pts]
        cs = [p[1] for p in pts]
        r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
        border = set()
        for j in range(c0, c1 + 1):
            border.add((r0, j))
            border.add((r1, j))
        for i in range(r0, r1 + 1):
            border.add((i, c0))
            border.add((i, c1))
        return set(pts) == border
    frame_color = None
    for c in coords_by_color:
        if is_frame(c):
            frame_color = c
            break
    pts = coords_by_color[frame_color]
    rs = [p[0] for p in pts]
    cs = [p[1] for p in pts]
    r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
    cropped = []
    for i in range(r0, r1 + 1):
        row = []
        for j in range(c0, c1 + 1):
            v = grid[i][j]
            if v == frame_color:
                row.append(3)
            else:
                row.append(v)
        cropped.append(row)
    return cropped