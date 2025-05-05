from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    visited = [[False]*W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 1 and not visited[r][c]:
                stack = [(r, c)]
                visited[r][c] = True
                region = []
                touches_border = False
                seeds = set()
                while stack:
                    rr, cc = stack.pop()
                    region.append((rr, cc))
                    if rr == 0 or rr == H-1 or cc == 0 or cc == W-1:
                        touches_border = True
                    v = grid[rr][cc]
                    if v not in (0, 1):
                        seeds.add(v)
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and grid[nr][nc] != 1:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                if not touches_border and len(seeds) == 1:
                    color = seeds.pop()
                    for rr, cc in region:
                        if res[rr][cc] != 1:
                            res[rr][cc] = color
    return res