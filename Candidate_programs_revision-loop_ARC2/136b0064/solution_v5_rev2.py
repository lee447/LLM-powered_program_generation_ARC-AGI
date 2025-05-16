from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cut = next(c for c in range(w) if any(row[c] == 4 for row in grid))
    out = [[0]*cut for _ in range(h)]
    # copy the right‐side "seed" shapes
    for i in range(h):
        for j in range(cut+1, w):
            v = grid[i][j]
            if v != 0 and v != 4:
                out[i][j-cut-1] = v
    # find contiguous nonempty blocks on left
    has = [any(grid[i][j] != 0 for j in range(cut)) for i in range(h)]
    blocks = []
    i = 0
    while i < h:
        if has[i]:
            j = i
            while j < h and has[j]:
                j += 1
            blocks.append((i, j))
            i = j
        else:
            i += 1
    for rs, re in blocks:
        # collect left‐side colors in block
        colors = {}
        for i in range(rs, re):
            for j in range(cut):
                v = grid[i][j]
                if v != 0:
                    colors.setdefault(v, []).append((i,j))
        if not colors:
            continue
        # pick the color whose points form a straight line (horiz or vert)
        pick = None
        for c, pts in colors.items():
            rows = {p[0] for p in pts}
            cols = {p[1] for p in pts}
            if len(rows)==1 or len(cols)==1:
                pick = c
                break
        if pick is None:
            continue
        pts = colors[pick]
        # if horizontal, rotate to vertical; if vertical, rotate to horizontal
        rows = {p[0] for p in pts}
        cols = {p[1] for p in pts}
        if len(rows)==1:
            # horizontal → vertical
            r0 = min(p[0] for p in pts)
            length = len(cols)
            c0 = min(p[1] for p in pts)
            offset = c0
            for k in range(length):
                out[rs+k][offset] = pick
        else:
            # vertical → horizontal
            c0 = min(p[1] for p in pts)
            length = len(rows)
            for k in range(length):
                out[rs][c0 + k] = pick
    return out