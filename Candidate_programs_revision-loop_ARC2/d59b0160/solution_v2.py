def solve(grid):
    n, m = len(grid), len(grid[0])
    bg = max(range(10), key=lambda c: sum(row.count(c) for row in grid))
    cross = [(i,j) for i in range(n) for j in range(m) if grid[i][j]==3]
    r0 = max(i for i,j in cross)
    c0 = max(j for i,j in cross)
    def quad(i,j):
        if i<r0 and j<c0: return 1
        if i<r0 and j>c0: return 2
        if i>r0 and j<c0: return 3
        if i>r0 and j>c0: return 4
        return 0
    cnt = {q:0 for q in (2,3,4)}
    for i in range(n):
        for j in range(m):
            q = quad(i,j)
            if q in cnt and grid[i][j]!=bg and grid[i][j]!=3:
                cnt[q] += 1
    rem = max(cnt, key=lambda q: cnt[q])
    out = [[grid[i][j] for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if quad(i,j)==rem and out[i][j]!=3:
                out[i][j] = bg
    return out