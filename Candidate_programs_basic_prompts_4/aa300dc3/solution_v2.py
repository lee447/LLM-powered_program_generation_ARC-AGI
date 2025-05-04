from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    best = []
    m, n = len(grid), len(grid[0])
    dirs = [(1,1),(1,-1)]
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 0:
                for dr, dc in dirs:
                    seq = []
                    rr, cc = r, c
                    while 0 <= rr < m and 0 <= cc < n and grid[rr][cc] == 0:
                        seq.append((rr, cc))
                        rr += dr
                        cc += dc
                    if len(seq) > len(best):
                        best = seq
    for r, c in best:
        grid[r][c] = 8
    return grid