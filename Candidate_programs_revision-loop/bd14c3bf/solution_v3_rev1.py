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
                minr = i
                minc = j
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
    if not clusters:
        return [row[:] for row in grid]
    band_h = h // 3
    keep = set()
    for b in range(3):
        block = [(r0,c0,comp) for (r0,c0,comp) in clusters if b*band_h <= r0 < (b+1)*band_h]
        if not block:
            continue
        block.sort(key=lambda x: x[1])
        k = len(block)
        idx = k // 2
        for (_,_,comp) in ([block[idx]] if k>1 else block):
            for p in comp:
                keep.add(p)
    res = [row[:] for row in grid]
    for _,_,comp in clusters:
        for r,c in comp:
            if (r,c) not in keep:
                res[r][c] = target
    return res