from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bw = w // 3
    regions = [[0] * 3 for _ in range(3)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for bx in range(3):
        sub = [row[bx*bw:(bx+1)*bw] for row in grid]
        visited = [[False]*bw for _ in range(h)]
        for y in range(h):
            for x in range(bw):
                c = sub[y][x]
                if c == 0 or visited[y][x]:
                    continue
                stack = [(y,x)]
                comp = []
                visited[y][x] = True
                while stack:
                    yy, xx = stack.pop()
                    comp.append((yy,xx))
                    for dy,dx in dirs:
                        ny, nx = yy+dy, xx+dx
                        if 0 <= ny < h and 0 <= nx < bw and not visited[ny][nx] and sub[ny][nx] == c:
                            visited[ny][nx] = True
                            stack.append((ny,nx))
                if len(comp) >= 3:
                    ys = [p[0] for p in comp]
                    top, bot = min(ys), max(ys)
                    if bot < h/3:
                        ry = 0
                    elif top >= 2*h/3:
                        ry = 2
                    else:
                        ry = 1
                    regions[ry][bx] = c
    return regions