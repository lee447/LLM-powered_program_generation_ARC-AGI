def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = 8
    pts = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != bg:
                pts.setdefault(c, []).append((i, j))
    shapes = {}
    for c, lst in pts.items():
        rs = [p[0] for p in lst]
        cs = [p[1] for p in lst]
        r0, c0 = min(rs), min(cs)
        shapes[c] = [(r - r0, c - c0) for r, c in lst]
    order = [1, 2, 3]
    others = [c for c in shapes if c not in order]
    order = order + others
    pos_map = {}
    pos_map[3] = "TL"
    pos_map[1] = "BL"
    pos_map[2] = "BR"
    for c in shapes:
        if c not in pos_map:
            pos_map[c] = "TR"
    quads = {"TL": [], "TR": [], "BL": [], "BR": []}
    for c, rel in shapes.items():
        quads[pos_map[c]] = (c, rel)
    def box(q):
        if not q: return (0,0)
        _, pts = q
        rs = [p[0] for p in pts]
        cs = [p[1] for p in pts]
        return (max(rs)+1, max(cs)+1)
    hTL, wTL = box(quads["TL"])
    hTR, wTR = box(quads["TR"])
    hBL, wBL = box(quads["BL"])
    hBR, wBR = box(quads["BR"])
    H = hTL + 1 + hBL
    W = wTL + 1 + wTR
    out = [[bg]*W for _ in range(H)]
    def place(q, off_r, off_c):
        if not q: return
        c, pts = q
        for dr, dc in pts:
            out[off_r+dr][off_c+dc] = c
    place(quads["TL"], 0, 0)
    place(quads["TR"], 0, wTL+1)
    place(quads["BL"], hTL+1, 0)
    place(quads["BR"], hTL+1, wTL+1)
    return out