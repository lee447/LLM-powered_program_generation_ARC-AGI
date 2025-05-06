from collections import deque
def solve(grid):
    H, W = len(grid), len(grid[0])
    eight_positions = [(i,j) for i in range(H) for j in range(W) if grid[i][j]==8]
    if not eight_positions:
        return []
    visited = [[False]*W for _ in range(H)]
    q = deque([eight_positions[0]])
    visited[eight_positions[0][0]][eight_positions[0][1]] = True
    cluster = [eight_positions[0]]
    while q:
        i,j = q.popleft()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i+di, j+dj
            if 0<=ni<H and 0<=nj<W and not visited[ni][nj] and grid[ni][nj]==8:
                visited[ni][nj] = True
                q.append((ni,nj))
                cluster.append((ni,nj))
    rows = [p[0] for p in cluster]
    cols = [p[1] for p in cluster]
    minr, maxr = min(rows), max(rows)
    minc, maxc = min(cols), max(cols)
    h, w = maxr-minr+1, maxc-minc+1
    counts = {}
    for i in range(H-h+1):
        for j in range(W-w+1):
            good = True
            key = []
            for di in range(h):
                row = grid[i+di][j:j+w]
                if 8 in row:
                    good = False
                    break
                key.append(tuple(row))
            if not good:
                continue
            key = tuple(key)
            if key in counts:
                counts[key][0] += 1
            else:
                counts[key] = [1, (i, j)]
    bestc = max(v[0] for v in counts.values())
    candidates = [(k, v[1]) for k,v in counts.items() if v[0]==bestc]
    if len(candidates)==1:
        best = candidates[0][0]
    else:
        best = min(candidates, key=lambda kv: abs(kv[1][0]-minr)+abs(kv[1][1]-minc))[0]
    return [list(row) for row in best]