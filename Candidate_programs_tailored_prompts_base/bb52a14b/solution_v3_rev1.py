from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    seeds = [(i,j) for i in range(h) for j in range(w) if grid[i][j]==8]
    cnts = [(sum(1 for di,dj in dirs if 0<=i+di<h and 0<=j+dj<w and grid[i+di][j+dj]==4),i,j) for i,j in seeds]
    if not cnts: return [row[:] for row in grid]
    mc = max(c for c,_,_ in cnts)
    if mc==0: return [row[:] for row in grid]
    ti,tj = next((i,j) for c,i,j in cnts if c==mc)
    T = [(di,dj) for di,dj in dirs if 0<=ti+di<h and 0<=tj+dj<w and grid[ti+di][tj+dj]==4]
    B = [(di,dj) for di,dj in dirs if 0<=ti+di<h and 0<=tj+dj<w and grid[ti+di][tj+dj]==1]
    for i,j in seeds:
        if i==ti and j==tj: continue
        if all(0<=i+di<h and 0<=j+dj<w and grid[i+di][j+dj]==1 for di,dj in B) and all(0<=i+di<h and 0<=j+dj<w and grid[i+di][j+dj]!=8 for di,dj in T):
            ti,tj = i,j
            break
    out = [row[:] for row in grid]
    for di,dj in T:
        out[ti+di][tj+dj] = 4
    return out