def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import defaultdict, deque
    cells = defaultdict(list)
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != 0:
                cells[c].append((i, j))
    def bbox(pts):
        rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
        return min(rs), max(rs), min(cs), max(cs)
    # find stick: a color whose points form a straight line (w==1 or h==1), choose longest
    stick = None
    best = -1
    for c, pts in cells.items():
        r0, r1, c0, c1 = bbox(pts)
        length = len(pts)
        if (r0 == r1 or c0 == c1) and length > best:
            best = length; stick = c
    # other colors
    branches = [c for c in cells if c != stick]
    # find branch1: one touching stick
    stset = set(cells[stick])
    b1 = None
    for c in branches:
        for p in cells[c]:
            for d in ((1,0),(-1,0),(0,1),(0,-1)):
                if (p[0]+d[0], p[1]+d[1]) in stset:
                    b1 = c
                    break
            if b1 is not None:
                break
        if b1 is not None:
            break
    b2 = [c for c in branches if c != b1][0]
    # pivot at stick-branch1 adjacency
    pivot = None
    for p in cells[b1]:
        for d in ((1,0),(-1,0),(0,1),(0,-1)):
            q = (p[0]+d[0], p[1]+d[1])
            if q in stset:
                pivot = q
                branch1_attach = p
                break
        if pivot: break
    # rotate branch1 90° cw about pivot
    def rot90(pts, piv):
        out = []
        pr, pc = piv
        for r, c in pts:
            dr, dc = r-pr, c-pc
            nr, nc = dc, -dr
            out.append((pr+nr, pc+nc))
        return out
    # rotate branch2 180° about pivot
    def rot180(pts, piv):
        pr, pc = piv
        return [(pr-(r-pr), pc-(c-pc)) for r,c in pts]
    new = [[0]*w for _ in range(h)]
    for i,j in cells[stick]:
        new[i][j] = stick
    b1_new = rot90(cells[b1], pivot)
    for i,j in b1_new:
        new[i][j] = b1
    b2_new = rot180(cells[b2], pivot)
    for i,j in b2_new:
        new[i][j] = b2
    return new