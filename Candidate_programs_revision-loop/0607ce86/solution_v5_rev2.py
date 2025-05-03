from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    out = [[0]*C for _ in range(R)]
    rows_mask = [any(cell != 0 for cell in row) for row in grid]
    row_intervals = []
    r = 0
    while r < R:
        if not rows_mask[r]:
            r += 1
            continue
        r0 = r
        while r+1 < R and rows_mask[r+1]:
            r += 1
        row_intervals.append((r0, r))
        r += 1
    for r0, r1 in row_intervals:
        H = r1 - r0 + 1
        cols_mask = [any(grid[r][c] != 0 for r in range(r0, r1+1)) for c in range(C)]
        col_intervals = []
        c = 0
        while c < C:
            if not cols_mask[c]:
                c += 1
                continue
            c0 = c
            while c+1 < C and cols_mask[c+1]:
                c += 1
            col_intervals.append((c0, c))
            c += 1
        widths = [c1 - c0 + 1 for c0, c1 in col_intervals]
        freq = {}
        for w in widths:
            if w > 1:
                freq[w] = freq.get(w, 0) + 1
        valid = [w for w, ct in freq.items() if ct == 2]
        if not valid:
            continue
        w = valid[0]
        selected = [(c0, c1) for c0, c1 in col_intervals if c1 - c0 + 1 == w]
        P = [[0]*w for _ in range(H)]
        for c0, c1 in selected:
            for i in range(H):
                for j in range(w):
                    v = grid[r0+i][c0+j]
                    if v != 0:
                        P[i][j] = v
        for c0, c1 in selected:
            for i in range(H):
                for j in range(w):
                    out[r0+i][c0+j] = P[i][j]
    return out