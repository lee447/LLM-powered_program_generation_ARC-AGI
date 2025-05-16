from collections import Counter, deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    flat_all = [c for row in grid for c in row]
    bg = Counter(flat_all).most_common(1)[0][0]
    seps = []
    for c in range(w):
        col = [grid[r][c] for r in range(h)]
        if len(set(col)) == 1 and col[0] != bg:
            seps.append(c)
    seps.sort()
    if len(seps) >= 2:
        start, end = seps[0] + 1, seps[1]
    else:
        start, end = 0, w
    block = [row[start:end] for row in grid]
    bh, bw = len(block), len(block[0])
    flatb = [c for row in block for c in row]
    bgb = Counter(flatb).most_common(1)[0][0]
    cnt = Counter(flatb)
    cnt.pop(bgb, None)
    if not cnt:
        return block
    color = max(cnt, key=cnt.get)
    vis = [[False]*bw for _ in range(bh)]
    comps = []
    for i in range(bh):
        for j in range(bw):
            if block[i][j] == color and not vis[i][j]:
                q = deque([(i, j)])
                vis[i][j] = True
                comp = []
                while q:
                    x, y = q.popleft()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < bh and 0 <= ny < bw and not vis[nx][ny] and block[nx][ny] == color:
                            vis[nx][ny] = True
                            q.append((nx, ny))
                comps.append(comp)
    if not comps:
        return block
    comp = max(comps, key=len)
    out = [[bgb]*bw for _ in range(bh)]
    for x, y in comp:
        out[x][y] = color
    return out