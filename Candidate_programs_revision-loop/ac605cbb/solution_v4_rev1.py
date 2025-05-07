from collections import defaultdict

def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    grey_count = defaultdict(int)
    grey_positions = []
    endpoints = []
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v == 1:
                path = [(r, c+1), (r, c+2)]
                ep = (r-1, c+2, 1)
            elif v == 2:
                path = [(r, c-1), (r, c-2), (r, c-3)]
                ep = (r, c-4, 2)
            elif v == 3:
                path = [(r+1, c), (r+2, c)]
                ep = (r+3, c, 3)
            elif v == 6:
                path = [(r-i, c) for i in (1,2,3,4,5)]
                ep = (r-6, c, 6)
            else:
                continue
            for rr, cc in path:
                if 0 <= rr < h and 0 <= cc < w:
                    grey_count[(rr, cc)] += 1
                    grey_positions.append((rr, cc))
            rr, cc, vv = ep
            if 0 <= rr < h and 0 <= cc < w:
                endpoints.append((rr, cc, vv))
    for rr, cc in grey_positions:
        if grid[rr][cc] == 0:
            out[rr][cc] = 4 if grey_count[(rr, cc)] > 1 else 5
    for rr, cc, vv in endpoints:
        out[rr][cc] = vv
    for (rr, cc), cnt in grey_count.items():
        if cnt > 1:
            i = 1
            while True:
                r2, c2 = rr + i, cc - i
                if 0 <= r2 < h and 0 <= c2 < w and out[r2][c2] == 0:
                    out[r2][c2] = 4
                    i += 1
                else:
                    break
    return out