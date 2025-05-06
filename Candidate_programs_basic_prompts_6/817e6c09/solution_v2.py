from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    blocks = []
    for r in range(R-1):
        for c in range(C-1):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                blocks.append((r,c))
    n = len(blocks)
    dp = [1]*n
    prev = [-1]*n
    for i in range(n):
        for j in range(i):
            if blocks[j][0] < blocks[i][0] and blocks[j][1] < blocks[i][1] and dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
                prev[i] = j
    if n:
        best = max(range(n), key=lambda i: dp[i])
        chain = set()
        i = best
        while i != -1:
            chain.add(blocks[i])
            i = prev[i]
    else:
        chain = set()
    out = [row[:] for row in grid]
    for r,c in blocks:
        if (r,c) in chain:
            out[r][c]=out[r][c+1]=out[r+1][c]=out[r+1][c+1]=8
    return out