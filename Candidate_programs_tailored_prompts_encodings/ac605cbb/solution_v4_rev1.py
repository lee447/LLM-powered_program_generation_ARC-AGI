from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    pts = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0]
    out = [[0]*w for _ in range(h)]
    for r, c, v in pts:
        out[r][c] = v
    occupied = {(r, c) for r, c, _ in pts}
    for r, c, v in pts:
        best = None
        for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            seg = []
            nr, nc = r+dr, c+dc
            while 0 <= nr < h and 0 <= nc < w and (nr, nc) not in occupied:
                seg.append((nr, nc))
                nr += dr
                nc += dc
            if seg:
                length = len(seg)
                end = seg[-1]
                if best is None or length > best[0]:
                    best = (length, seg, end)
        if best:
            length, seg, (er, ec) = best
            out[er][ec] = v
            mid = length // 2
            for i, (rr, cc) in enumerate(seg):
                out[rr][cc] = 4 if i == mid else 5
    return out