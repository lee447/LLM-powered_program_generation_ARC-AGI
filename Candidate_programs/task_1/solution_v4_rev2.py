from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    vis = [[False]*C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0 and not vis[i][j]:
                stack = [(i,j)]
                vis[i][j] = True
                cells = []
                while stack:
                    r, c = stack.pop()
                    cells.append((r,c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != 0 and not vis[nr][nc]:
                            vis[nr][nc] = True
                            stack.append((nr,nc))
                rmin = min(r for r,c in cells); rmax = max(r for r,c in cells)
                cmin = min(c for r,c in cells); cmax = max(c for r,c in cells)
                h = rmax - rmin + 1; w = cmax - cmin + 1
                if h*w == len(cells):
                    comps.append((rmin, cmin, h, w))
    comps = [(r,c,h,w) for r,c,h,w in comps if h>1 and w>1]
    size_count = {}
    for _,_,h,w in comps:
        size_count[(h,w)] = size_count.get((h,w),0) + 1
    if not size_count:
        return [[0]*C for _ in range(R)]
    target_h, target_w = max(size_count.keys(), key=lambda k: size_count[k])
    out = [[0]*C for _ in range(R)]
    for r0, c0, h, w in comps:
        if (h, w) == (target_h, target_w):
            for di in range(h):
                for dj in range(w):
                    out[r0+di][c0+dj] = grid[r0+di][c0+dj]
    return out