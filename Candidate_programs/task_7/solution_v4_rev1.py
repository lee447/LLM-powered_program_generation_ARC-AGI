import copy

def solve(grid):
    H, W = len(grid), len(grid[0])
    sep = 4
    # all separators (small+big)
    rows_all = [i for i in range(H) if sum(1 for x in grid[i] if x == sep) > W*2//3]
    cols_all = [j for j in range(W) if sum(1 for i in range(H) if grid[i][j] == sep) > H*2//3]
    rcuts_all = [-1] + rows_all + [H]
    ccuts_all = [-1] + cols_all + [W]
    # global separators (big‐block boundaries)
    rows_big = [i for i in range(H) if all(grid[i][j] == sep for j in range(W))]
    cols_big = [j for j in range(W) if all(grid[i][j] == sep for i in range(H))]
    rcuts_big = [-1] + rows_big + [H]
    ccuts_big = [-1] + cols_big + [W]
    # find big‐block segment
    rh = [rcuts_big[i+1] - rcuts_big[i] - 1 for i in range(len(rcuts_big)-1)]
    ch = [ccuts_big[j+1] - ccuts_big[j] - 1 for j in range(len(ccuts_big)-1)]
    bi = max(range(len(rh)), key=lambda i: rh[i])
    bj = max(range(len(ch)), key=lambda j: ch[j])
    r0 = rcuts_big[bi] + 1
    r1 = rcuts_big[bi+1] - 1
    c0 = ccuts_big[bj] + 1
    c1 = ccuts_big[bj+1] - 1
    arr = [row[c0+1:c1] for row in grid[r0+1:r1]]
    R = len(arr)
    C = len(arr[0]) if R else 0
    # which all‐segments cover the big block:
    big_rows = [i for i in range(len(rcuts_all)-1)
                if not (rcuts_all[i+1]-1 < r0 or rcuts_all[i]+1 > r1)]
    big_cols = [j for j in range(len(ccuts_all)-1)
                if not (ccuts_all[j+1]-1 < c0 or ccuts_all[j]+1 > c1)]
    bi0, bj0 = big_rows[0], big_cols[0]
    hcount = len(big_rows)
    wcount = len(big_cols)
    out = copy.deepcopy(grid)
    for i in range(len(rcuts_all)-1):
        for j in range(len(ccuts_all)-1):
            if i in big_rows and j in big_cols:
                continue
            rr = i if i < bi0 else (i - hcount if i >= bi0 + hcount else i)
            cc = j if j < bj0 else (j - wcount if j >= bj0 + wcount else j)
            if rr < 0 or rr >= R or cc < 0 or cc >= C:
                continue
            color = arr[rr][cc]
            if color == 0:
                continue
            rstart = rcuts_all[i] + 1
            cstart = ccuts_all[j] + 1
            for di in range(3):
                for dj in range(3):
                    r = rstart + di
                    c = cstart + dj
                    if 0 <= r < H and 0 <= c < W and grid[r][c] == 1:
                        out[r][c] = color
    return out