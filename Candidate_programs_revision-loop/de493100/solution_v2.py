def solve(grid):
    from collections import Counter
    n, m = len(grid), len(grid[0])
    # find marker color (full solid region)
    marker = None
    for c in set(x for row in grid for x in row):
        pts = [(i,j) for i in range(n) for j in range(m) if grid[i][j]==c]
        if not pts: continue
        rs = [i for i,_ in pts]; cs = [j for _,j in pts]
        h = max(rs)-min(rs)+1; w = max(cs)-min(cs)+1
        if h*w==len(pts) and len(pts)>1:
            if marker is None or len(pts)>sum(1 for row in grid for x in row if x==marker):
                marker = c; br, bc, hr, hc = min(rs), min(cs), h, w
    # helper to get windows
    def best_window(h, w):
        cnt = Counter()
        pos = {}
        for i in range(0, n-h+1, 1):
            for j in range(0, m-w+1, 1):
                block = tuple(tuple(grid[i+di][j+dj] for dj in range(w)) for di in range(h))
                if marker is not None and any(grid[i+di][j+dj]==marker for di in range(h) for dj in range(w)):
                    continue
                cnt[block] += 1
                pos[block] = block
        if not cnt: return None
        return cnt.most_common(1)[0][0]
    # candidates
    cands = []
    if marker is not None:
        h0, w0 = hr, hc
        for dh in range(0,3):
            for dw in range(0,3):
                h1, w1 = h0-dh, w0-dw
                if h1>0 and w1>0:
                    cands.append((h1,w1))
    # also try divisors
    for h in range(1, n+1):
        if n%h==0:
            for w in range(1, m+1):
                if m%w==0:
                    cands.append((h,w))
    seen = set()
    best = None
    for h,w in cands:
        if (h,w) in seen: continue
        seen.add((h,w))
        win = best_window(h,w)
        if win is not None:
            best = win
            break
    return [list(row) for row in best]