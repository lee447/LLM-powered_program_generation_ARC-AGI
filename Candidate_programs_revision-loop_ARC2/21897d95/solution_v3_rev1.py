import itertools
def solve(grid):
    H, W = len(grid), len(grid[0])
    row_runs = []
    i = 0
    while i < H:
        j = i + 1
        while j < H and grid[j] == grid[i]:
            j += 1
        row_runs.append((i, j))
        i = j
    col_runs = []
    j = 0
    while j < W:
        k = j + 1
        while k < W and all(grid[r][k] == grid[r][j] for r in range(H)):
            k += 1
        col_runs.append((j, k))
        j = k
    out_h = sum(c2 - c1 for c1, c2 in col_runs)
    out_w = sum(r2 - r1 for r1, r2 in row_runs)
    out = [[0] * out_w for _ in range(out_h)]
    for bi, (r1, r2) in enumerate(row_runs):
        for bj, (c1, c2) in enumerate(col_runs):
            block = [grid[r][c] for r in range(r1, r2) for c in range(c1, c2)]
            cnt = {}
            for x in block:
                cnt[x] = cnt.get(x, 0) + 1
            color = max(cnt.items(), key=lambda x: x[1])[0]
            obi = len(col_runs) - 1 - bj
            obj = bi
            tr1 = sum(c2 - c1 for c1, c2 in col_runs[:obi])
            tc1 = sum(r2 - r1 for r1, r2 in row_runs[:obj])
            for rr in range(tr1, tr1 + (c2 - c1)):
                for cc in range(tc1, tc1 + (r2 - r1)):
                    out[rr][cc] = color
    return out