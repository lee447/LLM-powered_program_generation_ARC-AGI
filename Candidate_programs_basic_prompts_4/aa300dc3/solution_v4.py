from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    dirs = [(1,1),(1,-1)]
    best_chain = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0: continue
            for dx, dy in dirs:
                pi, pj = i-dx, j-dy
                if 0 <= pi < n and 0 <= pj < m and grid[pi][pj] == 0: continue
                chain = []
                x, y = i, j
                while 0 <= x < n and 0 <= y < m and grid[x][y] == 0:
                    chain.append((x,y))
                    x += dx; y += dy
                if len(chain) > len(best_chain):
                    best_chain = chain
    out = [row[:] for row in grid]
    for i, j in best_chain:
        out[i][j] = 8
    return out