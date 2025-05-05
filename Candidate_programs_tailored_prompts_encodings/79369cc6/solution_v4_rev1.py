from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    visited = [[False]*W for _ in range(H)]
    clusters = []
    for i in range(H):
        for j in range(W):
            if orig[i][j] == 6 and not visited[i][j]:
                comp = []
                stack = [(i,j)]
                visited[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and orig[nr][nc] == 6:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                if len(comp) > 1:
                    clusters.append(comp)
    new4 = set()
    for comp in clusters:
        comp_sorted = sorted(comp, key=lambda x: x[0]+x[1], reverse=True)
        for idx, (r,c) in enumerate(comp_sorted[:2]):
            if idx == 0:
                offs = ((0,1),(1,0),(1,1))
            else:
                offs = ((0,2),(1,1),(1,2))
            for dr,dc in offs:
                rr,cc = r+dr, c+dc
                if 0 <= rr < H and 0 <= cc < W and orig[rr][cc] != 6:
                    new4.add((rr,cc))
    out = [row[:] for row in orig]
    for r,c in new4:
        out[r][c] = 4
    return out