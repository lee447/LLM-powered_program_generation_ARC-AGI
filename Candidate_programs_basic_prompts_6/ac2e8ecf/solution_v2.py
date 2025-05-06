from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                color = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                pts = []
                while stack:
                    r,c = stack.pop()
                    pts.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==color:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
                r0,r1 = min(rs), max(rs)
                c0,c1 = min(cs), max(cs)
                shape = [[0]*(c1-c0+1) for _ in range(r1-r0+1)]
                for r,c in pts:
                    shape[r-r0][c-c0] = color
                clusters.append((color, r0, c0, shape))
    clusters.sort(key=lambda x: (x[0], x[1], x[2]))
    res = [[0]*w for _ in range(h)]
    cx = 0; cy = 0; row_h = 0
    for color,_,_,shape in clusters:
        sh = len(shape); sw = len(shape[0])
        if cx + sw > w:
            cx = 0
            cy += row_h + 1
            row_h = 0
        for i in range(sh):
            for j in range(sw):
                if shape[i][j] != 0 and 0<=cy+i<h and 0<=cx+j<w:
                    res[cy+i][cx+j] = shape[i][j]
        cx += sw + 1
        row_h = max(row_h, sh)
    return res