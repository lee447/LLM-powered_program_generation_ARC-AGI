from typing import List, Tuple
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    def inb(r,c): return 0<=r<R and 0<=c<C
    # find the 2x2 block of four distinct nonzero colors
    bi = bj = None
    block = {}
    for i in range(R-1):
        for j in range(C-1):
            s = {grid[i][j], grid[i][j+1], grid[i+1][j], grid[i+1][j+1]}
            if 0 in s or len(s)!=4: continue
            bi,bj = i,j
            block = {
                (0,0): grid[i][j],
                (0,1): grid[i][j+1],
                (1,0): grid[i+1][j],
                (1,1): grid[i+1][j+1]
            }
            break
        if bi is not None: break
    # find the border color and its connected region
    blkcols = set(block.values())
    border_color = None
    start = None
    for (dr,dc),(v) in block.items():
        r,c = bi+dr, bj+dc
        for d in dirs:
            rr,cc = r+d[0], c+d[1]
            if inb(rr,cc) and grid[rr][cc]!=0 and grid[rr][cc] not in blkcols:
                border_color = grid[rr][cc]
                start = (rr,cc)
                break
        if border_color is not None: break
    # flood-fill border region
    q = deque([start])
    seen = {start}
    border = []
    while q:
        r,c = q.popleft()
        border.append((r,c))
        for d in dirs:
            rr,cc = r+d[0], c+d[1]
            if inb(rr,cc) and (rr,cc) not in seen and grid[rr][cc]==border_color:
                seen.add((rr,cc))
                q.append((rr,cc))
    rs = [r for r,_ in border]
    cs = [c for _,c in border]
    minr,maxr = min(rs), max(rs)
    minc,maxc = min(cs), max(cs)
    w = maxc-minc+1
    # pattern size = border-width - 1
    p = w-1
    N = p*2
    out = [[0]*N for _ in range(N)]
    t = p
    # fill the N x N output by 4 triangular regions
    thr = p
    for i in range(N):
        for j in range(N):
            if i+j < thr:
                out[i][j] = block[(0,0)]
            elif i+j > thr + (p-1):
                out[i][j] = block[(1,1)]
            else:
                if j - i > p-1:
                    out[i][j] = block[(0,1)]
                elif i - j > p-1:
                    out[i][j] = block[(1,0)]
                else:
                    # on the middle band: decide by comparing (i - j)
                    if j > i:
                        out[i][j] = block[(0,1)]
                    else:
                        out[i][j] = block[(1,0)]
    return out