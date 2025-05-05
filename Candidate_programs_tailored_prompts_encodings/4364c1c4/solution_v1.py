def solve(grid):
    h, w = len(grid), len(grid[0])
    freq = {}
    for r in grid:
        for v in r:
            freq[v] = freq.get(v, 0) + 1
    bg = max(freq, key=lambda x: freq[x])
    visited = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and grid[i][j] != bg:
                col = grid[i][j]
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc]==col:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                shapes.append((min(r for r,c in comp), col, comp))
    shapes.sort(key=lambda x: x[0])
    out = [[bg]*w for _ in range(h)]
    for idx,(_,col,comp) in enumerate(shapes):
        dx = -1 if idx%2==0 else 1
        for r,c in comp:
            out[r][c+dx] = col
    return out