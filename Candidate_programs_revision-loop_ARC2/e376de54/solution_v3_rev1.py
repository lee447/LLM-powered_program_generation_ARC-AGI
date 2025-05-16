from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = max({v:0 for row in grid for v in row}, key=lambda _:0)
    freq = {}
    for r in range(h):
        for c in range(w):
            freq[grid[r][c]] = freq.get(grid[r][c], 0) + 1
    bg = max(freq, key=lambda k: freq[k])
    dirs = {"h":(0,1),"v":(1,0),"d1":(1,1),"d2":(1,-1)}
    def keyfunc(name, r, c):
        if name=="h": return r
        if name=="v": return c
        if name=="d1": return c-r
        return r+c
    by_color = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v!=bg:
                by_color.setdefault(v, []).append((r,c))
    best_dir = None
    best_sum = -1
    for name,(dr,dc) in dirs.items():
        s = 0
        for col, pts in by_color.items():
            groups = {}
            for r,c in pts:
                k = keyfunc(name,r,c)
                groups.setdefault(k, []).append((r,c))
            for g in groups.values():
                if len(g)>=2:
                    s += len(g)
        if s>best_sum:
            best_sum = s
            best_dir = name
    dr, dc = dirs[best_dir]
    groups_by_color = {}
    max_len = {}
    for col, pts in by_color.items():
        groups = {}
        for r,c in pts:
            k = keyfunc(best_dir, r, c)
            groups.setdefault(k, []).append((r,c))
        groups_by_color[col] = groups
        max_len[col] = max((len(g) for g in groups.values()), default=1)
    uniq = sorted(set(max_len.values()))
    L = uniq[-2] if len(uniq)>1 else uniq[0]
    ref_color = next(c for c,l in max_len.items() if l==L)
    out = [[bg]*w for _ in range(h)]
    for col in by_color:
        if col==ref_color:
            groups = groups_by_color[col]
            if best_dir in ("h","v") and len(groups)>1:
                if best_dir=="h":
                    ref_keys = [k for k,g in groups.items() if len(g)==L]
                    r0 = min(ref_keys)
                    pattern = sorted(c for _,c in groups[r0])
                    rows = [k for k,g in groups.items() if len(g)>1]
                    for r in rows:
                        for c in pattern:
                            if 0<=c<w:
                                out[r][c] = col
                else:
                    ref_keys = [k for k,g in groups.items() if len(g)==L]
                    c0 = min(ref_keys)
                    pattern = sorted(r for r,_ in groups[c0])
                    cols = [k for k,g in groups.items() if len(g)>1]
                    for c in cols:
                        for r in pattern:
                            if 0<=r<h:
                                out[r][c] = col
            else:
                for r,c in by_color[col]:
                    out[r][c] = col
    for col in by_color:
        if col==ref_color: continue
        groups = groups_by_color[col]
        if max_len[col]>L and len(groups)>1:
            for r,c in by_color[col]:
                out[r][c] = col
            continue
        for k, pts in groups.items():
            if best_dir=="h":
                r = k
                m = min(c for _,c in pts)
                for i in range(L):
                    c0 = m + i
                    if 0<=c0<w:
                        out[r][c0] = col
            elif best_dir=="v":
                c = k
                m = min(r for r,_ in pts)
                for i in range(L):
                    r0 = m + i
                    if 0<=r0<h:
                        out[r0][c] = col
            else:
                proj = [(r*dr + c*dc, r, c) for r,c in pts]
                _, er, ec = max(proj)
                sr, sc = er - dr*(L-1), ec - dc*(L-1)
                for i in range(L):
                    r0 = sr + dr*i
                    c0 = sc + dc*i
                    if 0<=r0<h and 0<=c0<w:
                        out[r0][c0] = col
    return out