import collections

def solve(grid):
    h, w = len(grid), len(grid[0])
    freq = collections.Counter(v for row in grid for v in row)
    bg = max(freq, key=freq.get)
    visited = [[False]*w for _ in range(h)]
    rects = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != bg and not visited[i][j]:
                c = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny]==c:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                rows = [x for x,_ in cells]
                cols = [y for _,y in cells]
                top, bottom = min(rows), max(rows)
                left, right = min(cols), max(cols)
                rects.append((top,bottom,left,right,c))
    out = [row[:] for row in grid]
    for top,bottom,left,right,c in rects:
        ih = bottom - top - 1
        if ih > 0 and ih % 2 == 1:
            mid = top + 1 + ih//2
            for x in range(left+1, right):
                if out[mid][x] == bg:
                    out[mid][x] = c
    return out