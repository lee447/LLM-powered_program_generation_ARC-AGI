def solve(grid):
    n, m = len(grid), len(grid[0])
    cnt = {}
    for r in grid:
        for v in r:
            if v:
                cnt[v] = cnt.get(v, 0) + 1
    C = max(cnt, key=cnt.get)
    def max_run_row(i):
        best = cur = 0
        for j in range(m):
            if grid[i][j] == C:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return best
    def max_run_col(j):
        best = cur = 0
        for i in range(n):
            if grid[i][j] == C:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return best
    mr = [max_run_row(i) for i in range(n)]
    Mc = max(mr)
    H = [i for i in range(n) if mr[i] == Mc]
    mc = [max_run_col(j) for j in range(m)]
    Nc = max(mc)
    V = [j for j in range(m) if mc[j] == Nc]
    out = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == C and i not in H and j not in V:
                out[i][j] = C
    for hi in range(len(H)-1):
        for vj in range(len(V)-1):
            top, bot = H[hi], H[hi+1]
            left, right = V[vj], V[vj+1]
            cycle = []
            cycle.append((top, left))
            for x in range(left+1, right+1):
                cycle.append((top, x))
            for y in range(top+1, bot+1):
                cycle.append((y, right))
            for x in range(right-1, left-1, -1):
                cycle.append((bot, x))
            for y in range(bot-1, top, -1):
                cycle.append((y, left))
            L = len(cycle)
            for idx, (r, c) in enumerate(cycle):
                if grid[r][c] == C:
                    nr, nc = cycle[(idx+1) % L]
                    out[nr][nc] = C
    return out