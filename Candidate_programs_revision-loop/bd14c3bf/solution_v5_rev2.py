from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    target = grid[0][0]
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                minr, minc = i, j
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    if r < minr: minr = r
                    if c < minc: minc = c
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == 1:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                clusters.append((minr, minc, comp))
    band_h = h // 3
    keep = set()
    for b in range(3):
        block = [(r0,c0,comp) for (r0,c0,comp) in clusters if b*band_h <= r0 < (b+1)*band_h]
        k = len(block)
        if k == 0: continue
        block.sort(key=lambda x: x[1])
        if k == 1:
            idx = 0
        elif k == 2:
            idx = 1
        else:
            idx = k//2
        for _,_,comp in block[:idx] + block[idx+1:]:
            pass
        for _,_,comp in [block[idx]]:
            for p in comp:
                keep.add(p)
    res = [row[:] for row in grid]
    for _,_,comp in clusters:
        for r,c in comp:
            if (r,c) not in keep:
                res[r][c] = target
    return res