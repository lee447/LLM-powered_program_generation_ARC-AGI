def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0]
    out = [[0]*w for _ in range(h)]
    for r, c, v in pts:
        out[r][c] = v
    occupied = set((r,c) for r,c,_ in pts)
    segments = []
    for r, c, v in pts:
        best = None
        for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            nr, nc = r+dr, c+dc
            seg = []
            while 0 <= nr < h and 0 <= nc < w and (nr,nc) not in occupied:
                seg.append((nr,nc))
                nr += dr
                nc += dc
            if seg:
                end = seg[-1]
                length = len(seg)
                if best is None or length < best[0]:
                    best = (length, seg, end)
        if best:
            length, seg, (er,ec) = best
            occupied.add((er,ec))
            out[er][ec] = v
            for i,(rr,cc) in enumerate(seg):
                out[rr][cc] = 4 if length>2 and i==length//2 else 5
    return out