def solve(grid):
    h, w = len(grid), len(grid[0])
    blocks = []
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j]==2 and grid[i][j+1]==2 and grid[i+1][j]==2 and grid[i+1][j+1]==2:
                blocks.append((i,j))
    n = len(blocks)
    inc_dp = [1]*n
    inc_prev = [-1]*n
    dec_dp = [1]*n
    dec_prev = [-1]*n
    for i in range(n):
        for j in range(i):
            if blocks[j][0]<blocks[i][0] and blocks[j][1]<blocks[i][1]:
                if inc_dp[j]+1>inc_dp[i]:
                    inc_dp[i]=inc_dp[j]+1
                    inc_prev[i]=j
            if blocks[j][0]<blocks[i][0] and blocks[j][1]>blocks[i][1]:
                if dec_dp[j]+1>dec_dp[i]:
                    dec_dp[i]=dec_dp[j]+1
                    dec_prev[i]=j
    def build(dp, prev):
        idx = max(range(n), key=lambda i: dp[i])
        path = set()
        while idx!=-1:
            path.add(idx)
            idx = prev[idx]
        return path
    inc_set = build(inc_dp, inc_prev)
    dec_set = build(dec_dp, dec_prev)
    sel = inc_set if len(inc_set)>=len(dec_set) else dec_set
    out = [row[:] for row in grid]
    for k in sel:
        i,j = blocks[k]
        out[i][j]=out[i][j+1]=out[i+1][j]=out[i+1][j+1]=8
    return out