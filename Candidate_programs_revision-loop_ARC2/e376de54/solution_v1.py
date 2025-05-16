from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = 7
    dirs = [((0,1),"h"), ((1,0),"v"), ((1,1),"d1"), ((1,-1),"d2")]
    # collect non-background points
    by_color = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v!=bg:
                by_color.setdefault(v, []).append((r,c))
    # find reference: max collinear run
    best = (None, None, None, 0)  # color, dir, key, length
    for col, pts in by_color.items():
        for (dr,dc),name in dirs:
            groups = {}
            for r,c in pts:
                if name=="h": key=r
                elif name=="v": key=c
                elif name=="d1": key=c-r
                else: key=r+c
                groups.setdefault(key, []).append((r,c))
            for key, g in groups.items():
                if len(g)>best[3]:
                    best = (col, (dr,dc), name, len(g))
    ref_col, (dr,dc), dname, L = best
    # build new grid
    out = [[bg]*w for _ in range(h)]
    # place reference as is
    for r,c in by_color.get(ref_col, []):
        out[r][c] = ref_col
    # adjust others
    for col, pts in by_color.items():
        if col==ref_col: continue
        # group by same direction
        groups = {}
        for r,c in pts:
            if dname=="h": key=r
            elif dname=="v": key=c
            elif dname=="d1": key=c-r
            else: key=r+c
            groups.setdefault(key, []).append((r,c))
        for key, g in groups.items():
            # check all lie on a line of that direction
            if len(g)<1: continue
            # project and sort
            t_sorted = sorted(g, key=lambda x: x[0]*dr + x[1]*dc)
            n = len(t_sorted)
            if n> L:
                keep = t_sorted[-L:]
                for r,c in keep:
                    out[r][c] = col
            elif n< L:
                # extend backwards
                p0 = t_sorted[0]
                adds = []
                for k in range(1, L-n+1):
                    nr = p0[0] - dr*k
                    nc = p0[1] - dc*k
                    if 0<=nr<h and 0<=nc<w and grid[nr][nc]==bg:
                        adds.append((nr,nc))
                for r,c in adds:
                    out[r][c] = col
                for r,c in t_sorted:
                    out[r][c] = col
            else:
                for r,c in t_sorted:
                    out[r][c] = col
    return out