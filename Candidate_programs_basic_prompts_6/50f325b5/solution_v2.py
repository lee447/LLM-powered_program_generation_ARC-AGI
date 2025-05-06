def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    counts = {}
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            counts[v] = counts.get(v, 0) + 1
    shape_color = None
    for c, cnt in sorted(counts.items(), key=lambda x: x[1]):
        if c != 0 and cnt > 1:
            shape_color = c
            break
    pts = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == shape_color]
    r0 = min(r for r, c in pts)
    c0 = min(c for r, c in pts)
    S0 = [(r - r0, c - c0) for r, c in pts]
    def normalize(S):
        drs = [dr for dr, dc in S]
        dcs = [dc for dr, dc in S]
        mdr = min(drs)
        mdc = min(dcs)
        return sorted([(dr - mdr, dc - mdc) for dr, dc in S])
    def rot90(S):
        return [(dc, -dr) for dr, dc in S]
    def rot180(S):
        return [(-dr, -dc) for dr, dc in S]
    def rot270(S):
        return [(-dc, dr) for dr, dc in S]
    shapes = []
    shapes.append(normalize(S0))
    shapes.append(normalize(rot90(S0)))
    shapes.append(normalize(rot180(S0)))
    shapes.append(normalize(rot270(S0)))
    orig = [row[:] for row in grid]
    to_fill = set()
    for S in shapes:
        maxdr = max(dr for dr, dc in S)
        maxdc = max(dc for dr, dc in S)
        dr0, dc0 = S[0]
        for i in range(rows - maxdr):
            for j in range(cols - maxdc):
                v = orig[i + dr0][j + dc0]
                if v == 0 or v == shape_color:
                    continue
                ok = True
                for dr, dc in S:
                    if orig[i + dr][j + dc] != v:
                        ok = False
                        break
                if ok:
                    for dr, dc in S:
                        to_fill.add((i + dr, j + dc))
    for r, c in to_fill:
        grid[r][c] = shape_color
    return grid