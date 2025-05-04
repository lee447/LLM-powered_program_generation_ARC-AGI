def solve(grid):
    h, w = len(grid), len(grid[0])
    comps = {}
    seen = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != 0 and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==c:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                xs = [x for x,y in cells]
                ys = [y for x,y in cells]
                comps[c] = (min(xs), max(xs), min(ys), max(ys))
    # choose color by heuristic: maximal (row_span + col_span), tie-break by highest color
    best = None
    best_score = -1
    for c,(r0,r1,c0,c1) in comps.items():
        score = (r1-r0+1)+(c1-c0+1)
        if score>best_score or (score==best_score and c>best):
            best_score, best = score, c
    r0,r1,c0,c1 = comps[best]
    return [row[c0:c1+1] for row in grid[r0:r1+1]]