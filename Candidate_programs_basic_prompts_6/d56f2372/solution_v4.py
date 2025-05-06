def solve(grid):
    H = len(grid)
    W = len(grid[0])
    seen = [[False]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not seen[i][j]:
                col = grid[i][j]
                pts = []
                stack = [(i,j)]
                seen[i][j] = True
                while stack:
                    x,y = stack.pop()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not seen[nx][ny] and grid[nx][ny] == col:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                rs = [p[0] for p in pts]
                cs = [p[1] for p in pts]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                out = []
                for r in range(r0, r1+1):
                    row = []
                    for c in range(c0, c1+1):
                        row.append(grid[r][c])
                    out.append(row)
                return out
    return []