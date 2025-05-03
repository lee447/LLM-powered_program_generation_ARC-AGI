from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    def segments(r):
        segs = []
        c = 0
        while c < W:
            if grid[r][c] != 0:
                s = c
                while c < W and grid[r][c] != 0:
                    c += 1
                segs.append((s, c))
            else:
                c += 1
        return segs
    minWidth = 3
    valid = [False]*H
    rowSegs = [segments(r) for r in range(H)]
    for r in range(H):
        cnt = sum(1 for s,e in rowSegs[r] if e-s >= minWidth)
        if cnt >= 2:
            valid[r] = True
    stripes = []
    r = 0
    while r < H:
        if valid[r]:
            start = r
            while r+1 < H and valid[r+1]:
                r += 1
            stripes.append(list(range(start, r+1)))
        r += 1
    out = [[0]*W for _ in range(H)]
    for stripe in stripes:
        base = rowSegs[stripe[0]]
        segs = [s for s,e in base if e-s >= minWidth]
        segs = [(s,e) for s,e in base if e-s >= minWidth]
        for s,e in segs:
            freq = {}
            for r in stripe:
                for c in range(s, e):
                    v = grid[r][c]
                    if v:
                        freq[v] = freq.get(v,0) + 1
            if not freq: continue
            val = max(freq, key=lambda x: freq[x])
            for r in stripe:
                for c in range(s, e):
                    out[r][c] = val
    return out