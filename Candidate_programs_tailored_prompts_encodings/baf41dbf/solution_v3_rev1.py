from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    th, bh = h, -1
    lw, rw = w, -1
    anchors = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 3:
                th = min(th, r)
                bh = max(bh, r)
                lw = min(lw, c)
                rw = max(rw, c)
            elif grid[r][c] == 6:
                anchors.append((r, c))
    nt, nb, nl, nr = th, bh, lw, rw
    for r, c in anchors:
        if c > rw:
            nr = max(nr, c - 1)
        if c < lw:
            nl = min(nl, c + 1)
        if r > bh:
            nb = max(nb, r - 1)
        if r < th:
            nt = min(nt, r + 1)
    verts = [c for c in range(lw + 1, rw) if all(grid[r][c] == 3 for r in range(th, bh + 1))]
    spine_c = min(verts) if verts else None
    hors = [r for r in range(th + 1, bh) if all(grid[r][c] == 3 for c in range(lw, rw + 1))]
    spine_r = min(hors) if not spine_c and hors else None
    out = [[0] * w for _ in range(h)]
    for r, c in anchors:
        out[r][c] = 6
    for c in range(nl, nr + 1):
        if out[nt][c] == 0:
            out[nt][c] = 3
        if out[nb][c] == 0:
            out[nb][c] = 3
    for r in range(nt, nb + 1):
        if out[r][nl] == 0:
            out[r][nl] = 3
        if out[r][nr] == 0:
            out[r][nr] = 3
    if spine_c is not None:
        for r in range(nt, nb + 1):
            if out[r][spine_c] == 0:
                out[r][spine_c] = 3
    elif spine_r is not None:
        for c in range(nl, nr + 1):
            if out[spine_r][c] == 0:
                out[spine_r][c] = 3
    return out