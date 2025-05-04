def solve(grid):
    h, w = len(grid), len(grid[0])
    pts2 = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==2]
    if not pts2: return [row[:] for row in grid]
    r0 = min(r for r,c in pts2)
    c0 = min(c for r,c in pts2)
    H = max(r for r,c in pts2) - r0 + 1
    W = max(c for r,c in pts2) - c0 + 1
    S = set((r-r0,c-c0) for r,c in pts2)
    def rot180(S_,H_,W_):
        return set((H_-1-r,W_-1-c) for r,c in S_)
    S_rot = rot180(S,H,W)
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            # square corners of 4
            if r+H-1<h and c+W-1<w:
                ok = True
                for rr,cc in [(r,c),(r+H-1,c),(r,c+W-1),(r+H-1,c+W-1)]:
                    if grid[rr][cc]!=4: ok=False
                if ok:
                    for dr,dc in S:
                        out[r+dr][c+dc]=2
            # V apex up
            if r+2<H*2 and 0<c and c+0<w:
                if r+2<h and 0<c and c<w and grid[r][c]==4 and grid[r+2][c-1]==4 and grid[r+2][c+1]==4:
                    rr0,cc0 = r- (H-1), c-(W//2)
                    if 0<=rr0 and rr0+H<=h and 0<=cc0 and cc0+W<=w:
                        for dr,dc in S_rot:
                            out[rr0+dr][cc0+dc]=2
            # V apex down
            if r-(2)>=0 and 0<c and c<w:
                if grid[r][c]==4 and grid[r-2][c-1]==4 and grid[r-2][c+1]==4:
                    rr0,cc0 = r, c-(W//2)
                    if rr0+H<=h and 0<=cc0 and cc0+W<=w:
                        for dr,dc in S:
                            out[rr0+dr][cc0+dc]=2
    return out