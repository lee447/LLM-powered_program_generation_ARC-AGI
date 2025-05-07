import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    A = np.array(grid)
    dirs8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # find reference >1 component
    vis = np.zeros((h, w), bool)
    ref = []
    for i in range(h):
        for j in range(w):
            if A[i, j] > 1 and not vis[i, j]:
                stack = [(i, j)]
                vis[i, j] = True
                while stack:
                    r, c = stack.pop()
                    ref.append((r, c))
                    for dr, dc in dirs8:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < h and 0 <= nc < w and A[nr, nc] > 1 and not vis[nr, nc]:
                            vis[nr, nc] = True
                            stack.append((nr, nc))
                break
        if ref:
            break
    if not ref:
        return grid

    rs, cs = zip(*ref)
    r0, c0 = min(rs), min(cs)
    mask = {(r - r0, c - c0): A[r, c] for r, c in ref}

    # build all 8 dihedral transforms of mask
    trans = [
        lambda r, c: ( r,  c),
        lambda r, c: ( c, -r),
        lambda r, c: (-r, -c),
        lambda r, c: (-c,  r),
        lambda r, c: ( r, -c),
        lambda r, c: (-r,  c),
        lambda r, c: ( c,  r),
        lambda r, c: (-c, -r),
    ]
    masks = []
    for f in trans:
        pts = []
        for (r, c), col in mask.items():
            rr, cc = f(r, c)
            pts.append((rr, cc, col))
        minr = min(rr for rr, cc, col in pts)
        minc = min(cc for rr, cc, col in pts)
        norm = {}
        for rr, cc, col in pts:
            norm[(rr - minr, cc - minc)] = col
        masks.append((set(norm.keys()), norm))

    out = A.copy()
    vis1 = np.zeros((h, w), bool)
    for i in range(h):
        for j in range(w):
            if A[i, j] == 1 and not vis1[i, j]:
                stack = [(i, j)]
                vis1[i, j] = True
                comp = []
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    for dr, dc in dirs8:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < h and 0 <= nc < w and A[nr, nc] == 1 and not vis1[nr, nc]:
                            vis1[nr, nc] = True
                            stack.append((nr, nc))
                rs2, cs2 = zip(*comp)
                r1, c1 = min(rs2), min(cs2)
                offs = {(r - r1, c - c1) for r, c in comp}
                for keys, mp in masks:
                    if offs == keys:
                        for (dr, dc), col in mp.items():
                            out[r1 + dr, c1 + dc] = col
                        break
    return out.tolist()