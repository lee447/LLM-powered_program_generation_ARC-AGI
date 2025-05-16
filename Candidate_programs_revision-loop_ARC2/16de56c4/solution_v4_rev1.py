from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    out = [row[:] for row in grid]
    row_max = max(sum(1 for v in row if v != 0) for row in grid)
    col_max = max(sum(1 for i in range(h) if grid[i][j] != 0) for j in range(w))
    if row_max <= col_max:
        for i in range(h):
            R = [j for j, v in enumerate(grid[i]) if v != 0]
            if len(R) < 2:
                continue
            R.sort()
            diffs = [R[k+1] - R[k] for k in range(len(R) - 1)]
            d = diffs[0]
            for v in diffs[1:]:
                d = gcd(d, v)
            color = min(grid[i][j] for j in R)
            if len(R) == 2:
                offset = R[0] % d
                for c in range(offset, w, d):
                    out[i][c] = color
            else:
                mn, mx = R[0], R[-1]
                offset = R[0] % d
                for c in range(mn, mx + 1):
                    if (c - offset) % d == 0:
                        out[i][c] = color
    else:
        for j in range(w):
            R = [i for i in range(h) if grid[i][j] != 0]
            if len(R) < 2:
                continue
            R.sort()
            diffs = [R[k+1] - R[k] for k in range(len(R) - 1)]
            use = R
            if len(R) >= 3 and any(diffs[k] != diffs[0] for k in range(1, len(diffs))):
                groups = {}
                for i in R:
                    groups.setdefault(grid[i][j], []).append(i)
                best = []
                for rows_c in groups.values():
                    if len(rows_c) >= 2:
                        rows_c.sort()
                        d_c_list = [rows_c[k+1] - rows_c[k] for k in range(len(rows_c) - 1)]
                        if len(rows_c) == 2 or all(d_c_list[k] == d_c_list[0] for k in range(1, len(d_c_list))):
                            if len(rows_c) > len(best):
                                best = rows_c[:]
                if best:
                    use = best
                    diffs = [use[k+1] - use[k] for k in range(len(use) - 1)]
            d = diffs[0]
            for v in diffs[1:]:
                d = gcd(d, v)
            offset = use[0] % d
            color = max(grid[i][j] for i in use)
            for r in range(offset, h, d):
                out[r][j] = color
    return out