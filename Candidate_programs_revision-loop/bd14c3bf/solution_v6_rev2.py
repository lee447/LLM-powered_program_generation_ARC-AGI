from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def neighbors(r,c):
        for dr,dc in dirs:
            nr,nc = r+dr, c+dc
            if 0 <= nr < h and 0 <= nc < w:
                yield nr,nc
    def find_clusters(v: int):
        vis = [[False]*w for _ in range(h)]
        clusters = []
        for i in range(h):
            for j in range(w):
                if not vis[i][j] and grid[i][j] == v:
                    q = [(i,j)]
                    vis[i][j] = True
                    comp = [(i,j)]
                    for r,c in q:
                        for nr,nc in neighbors(r,c):
                            if not vis[nr][nc] and grid[nr][nc] == v:
                                vis[nr][nc] = True
                                q.append((nr,nc))
                                comp.append((nr,nc))
                    clusters.append(comp)
        return clusters
    out = [row[:] for row in grid]
    for cl in find_clusters(1):
        rs = [r for r,c in cl]; cs = [c for r,c in cl]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        H, W = r1-r0+1, c1-c0+1
        if H < 3 or W < 3:
            continue
        top_full = all(grid[r0][c] == 1 for c in range(c0, c1+1))
        bot_full = all(grid[r1][c] == 1 for c in range(c0, c1+1))
        left_full = all(grid[r][c0] == 1 for r in range(r0, r1+1))
        right_full = all(grid[r][c1] == 1 for r in range(r0, r1+1))
        fcount = sum((top_full, bot_full, left_full, right_full))
        if fcount == 3 or (top_full and bot_full and H >= 4) or (left_full and right_full and W >= 4):
            for r,c in cl:
                out[r][c] = 2
    return out