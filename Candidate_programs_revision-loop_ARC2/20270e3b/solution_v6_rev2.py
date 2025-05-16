from collections import deque
def solve(grid):
    H, W = len(grid), len(grid[0])
    def find_full1_col():
        for j in range(W):
            if all(grid[i][j] == 1 for i in range(H)):
                return j
        return None
    def find_full1_row():
        for i in range(H):
            if all(grid[i][j] == 1 for j in range(W)):
                return i
        return None
    def extract(rows, cols):
        sub = [[grid[i][j] for j in cols] for i in rows]
        R, C = len(rows), len(cols)
        barrier_cols = {j for i in range(R) for j in range(C) if sub[i][j] == 7}
        barrier_rows = {i for i in range(R) for j in range(C) if sub[i][j] == 7}
        vis = [[False]*C for _ in range(R)]
        found = False
        for i in range(R):
            for j in range(C):
                if sub[i][j] == 1 and i not in barrier_rows and j not in barrier_cols:
                    qi, qj = i, j
                    found = True
                    break
            if found: break
        if not found:
            return [[4]*C for _ in range(R)]
        dq = deque([(qi, qj)])
        vis[qi][qj] = True
        while dq:
            i, j = dq.popleft()
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = i+di, j+dj
                if 0 <= ni < R and 0 <= nj < C and not vis[ni][nj]:
                    if sub[ni][nj] == 1 and ni not in barrier_rows and nj not in barrier_cols:
                        vis[ni][nj] = True
                        dq.append((ni, nj))
        out = []
        for i in range(R):
            row = []
            for j in range(C):
                row.append(1 if vis[i][j] else 4)
            out.append(row)
        return out

    c1 = find_full1_col()
    if c1 is not None:
        cols = list(range(c1))
        rows = list(range(H))
        return extract(rows, cols)

    r1 = find_full1_row()
    if r1 is not None:
        top = [i for i in range(r1) if not all(grid[i][j] == 7 for j in range(W))]
        bot = [i for i in range(r1+1, H) if not all(grid[i][j] == 7 for j in range(W))]
        out1 = extract(top, list(range(W)))
        out2 = extract(bot, list(range(W)))
        return out1 + out2

    pts = [(i,j) for i in range(H) for j in range(W) if grid[i][j] == 1]
    if not pts:
        return [[4]]
    rs, cs = zip(*pts)
    r0 = max(0, min(rs)-1)
    r1 = min(H-1, max(rs)+1)
    c0 = max(0, min(cs)-1)
    c1 = min(W-1, max(cs)+1)
    out = []
    for i in range(r0, r1+1):
        row = []
        for j in range(c0, c1+1):
            row.append(1 if grid[i][j] == 1 else 4)
        out.append(row)
    return out