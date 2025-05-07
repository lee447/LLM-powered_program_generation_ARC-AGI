from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    zero_row = lambda i: all(grid[i][j] == 0 for j in range(W))
    zero_col = lambda j: all(grid[i][j] == 0 for i in range(H))
    row_seps = [i for i in range(H) if zero_row(i)]
    col_seps = [j for j in range(W) if zero_col(j)]
    br = [row_seps[k] + 1 for k in range(len(row_seps) - 1) if row_seps[k] + 1 < row_seps[k+1]]
    bc = [col_seps[k] + 1 for k in range(len(col_seps) - 1) if col_seps[k] + 1 < col_seps[k+1]]
    B = row_seps[1] - br[0]
    mid = (B - 1) // 2
    out = [row[:] for row in grid]
    nb = len(br)
    for bi, ri in enumerate(br):
        for bj, ci in enumerate(bc):
            cnt = {}
            for r in range(B):
                for c in range(B):
                    v = grid[ri + r][ci + c]
                    if v != 0:
                        cnt[v] = cnt.get(v, 0) + 1
            if not cnt:
                continue
            if len(cnt) == 1:
                minor = major = next(iter(cnt))
            else:
                items = sorted(cnt.items(), key=lambda x: x[1])
                minor, major = items[0][0], items[-1][0]
            for r in range(B):
                for c in range(B):
                    if bj == 0:
                        if bi < nb - 1:
                            cond = (r + c < mid)
                        else:
                            cond = (abs(c - mid) > (B - 1 - r))
                    elif bj == nb - 1:
                        if bi < nb - 1:
                            cond = (r + (B - 1 - c) < mid)
                        else:
                            cond = ((B - 1 - r) + (B - 1 - c) < mid)
                    else:
                        if bi < nb - 1:
                            cond = (abs(c - mid) > r)
                        else:
                            cond = (abs(c - mid) > (B - 1 - r))
                    out[ri + r][ci + c] = minor if cond else major
    return out