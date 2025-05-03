from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    out = [[0]*C for _ in range(R)]
    rows_nonzero = [any(cell != 0 for cell in row) for row in grid]
    r = 0
    while r < R:
        if not rows_nonzero[r]:
            r += 1
            continue
        r0 = r
        while r+1 < R and rows_nonzero[r+1]:
            r += 1
        r1 = r
        H = r1 - r0 + 1
        col_nonzero = [any(grid[i][j] != 0 for i in range(r0, r1+1)) for j in range(C)]
        raw = []
        c = 0
        while c < C:
            if col_nonzero[c]:
                c0 = c
                while c+1 < C and col_nonzero[c+1]:
                    c += 1
                raw.append((c0, c))
            c += 1
        widths = [c1-c0+1 for c0,c1 in raw]
        counts = {}
        for w in widths:
            if w > 1:
                counts[w] = counts.get(w, 0) + 1
        valid_ws = [w for w, ct in counts.items() if ct == 2]
        if valid_ws:
            w = valid_ws[0]
            intervals = [(c0, c1) for c0,c1 in raw if c1-c0+1 == w]
            P = [[0]*w for _ in range(H)]
            for c0,c1 in intervals:
                for i in range(H):
                    for j in range(w):
                        v = grid[r0+i][c0+j]
                        if v != 0:
                            P[i][j] = v
            for c0,c1 in intervals:
                for i in range(H):
                    for j in range(w):
                        out[r0+i][c0+j] = P[i][j]
        r += 1
    return out