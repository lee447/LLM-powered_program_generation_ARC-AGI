from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    clusters = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 1:
                clusters.setdefault(v, []).append((r, c))
    S = [(0,2),(0,3),(1,0),(1,1),(2,2)]
    def normalize(P):
        mr = min(r for r,c in P); mc = min(c for r,c in P)
        return sorted(((r-mr, c-mc) for r,c in P))
    def rot90(P):
        Q = [(c, -r) for r,c in P]
        return normalize(Q)
    def mirror(P):
        Q = [(r, -c) for r,c in P]
        return normalize(Q)
    variants = []
    base = normalize(S)
    mats = [base]
    for _ in range(3):
        mats.append(rot90(mats[-1]))
    for m in mats:
        variants.append(m)
        variants.append(mirror(m))
    variants = [list(dict.fromkeys(v)) for v in variants]
    for v, pts in clusters.items():
        if len(pts) == len(S):
            continue
        for shape in variants:
            for s in shape:
                r0 = pts[0][0] - s[0]
                c0 = pts[0][1] - s[1]
                ok = True
                for pr, pc in pts:
                    if (pr - r0, pc - c0) not in shape:
                        ok = False
                        break
                if not ok:
                    continue
                for dr, dc in shape:
                    rr, cc = r0 + dr, c0 + dc
                    if 0 <= rr < h and 0 <= cc < w:
                        out[rr][cc] = v
                break
            else:
                continue
            break
    return out