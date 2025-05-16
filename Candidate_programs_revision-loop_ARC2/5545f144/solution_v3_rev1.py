from collections import Counter, deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    seps = [c for c in range(w) if len({grid[r][c] for r in range(h)}) == 1]
    seps.sort()
    if len(seps) >= 2:
        start, end = seps[0] + 1, seps[1]
    else:
        start, end = 0, seps[0]
    block = [row[start:end] for row in grid]
    hh, ww = len(block), len(block[0])
    flat = [c for row in block for c in row]
    bg = Counter(flat).most_common(1)[0][0]
    cnt = Counter(flat)
    cnt.pop(bg, None)
    if not cnt:
        return block
    color = max(cnt, key=cnt.get)
    vis = [[False]*ww for _ in range(hh)]
    comps = []
    for i in range(hh):
        for j in range(ww):
            if block[i][j] == color and not vis[i][j]:
                q = deque([(i,j)])
                comp = []
                vis[i][j] = True
                while q:
                    x,y = q.popleft()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < hh and 0 <= ny < ww and not vis[nx][ny] and block[nx][ny] == color:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                comps.append(comp)
    if not comps:
        return block
    comp = max(comps, key=len)
    out = [[bg]*ww for _ in range(hh)]
    for x,y in comp:
        out[x][y] = color
    return out