from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    nonz = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    if not nonz:
        return []
    cols = sorted({c for _, c in nonz})
    best = None
    # split into two column‐clusters
    gaps = [(cols[i+1] - cols[i], i) for i in range(len(cols)-1)]
    gap, idx = max(gaps)
    if gap > 1:
        left = set(cols[:idx+1])
        right = set(cols[idx+1:])
    else:
        left = set(cols)
        right = left
    # choose the cluster with smaller height
    def bounds(cs):
        rs = [r for r,c in nonz if c in cs]
        return min(rs), max(rs)
    r0, r1 = bounds(left)
    s0, s1 = bounds(right)
    A = left if (r1-r0) < (s1-s0) else right
    rs = [r for r,c in nonz if c in A]
    cs = [c for r,c in nonz if c in A]
    rmin, rmax = min(rs), max(rs)
    cmin, cmax = min(cs), max(cs)
    sub = [[grid[r][c] for c in range(cmin, cmax+1)] for r in range(rmin, rmax+1)]
    H, W = len(sub), len(sub[0])
    # find borderpoints
    B = []
    for r in range(H):
        for c in range(W):
            if sub[r][c] != 0:
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    rr,cc = r+dr, c+dc
                    if rr<0 or rr>=H or cc<0 or cc>=W or sub[rr][cc]==0:
                        B.append((r,c))
                        break
    # horizontal runs endpoints
    from collections import defaultdict
    byrow = defaultdict(list)
    for r,c in B:
        byrow[r].append(c)
    Hpts = {}
    for r, vs in byrow.items():
        xs = sorted(set(vs))
        runs = []
        cur = [xs[0]]
        for x in xs[1:]:
            if x==cur[-1]+1:
                cur.append(x)
            else:
                runs.append(cur)
                cur=[x]
        runs.append(cur)
        ep = []
        for run in runs:
            if len(run)>=2:
                ep.append(run[0]); ep.append(run[-1])
            else:
                ep.append(run[0])
        Hpts[r] = sorted(set(ep))
    # build output: 3 rows
    top = Hpts.get(0, [])
    bot = Hpts.get(H-1, [])
    mid = sorted(set(top) | set(bot))
    out = [[0]*W for _ in range(3)]
    for c in top:
        out[0][c] = 8
        out[2][c] = 8
    for c in mid:
        out[1][c] = 8
    return out